#!/usr/bin/env python3
"""
merge_zotero.py
Merge two Zotero-exported JSON files and remove duplicates.

Reads:
  - dart-publications-sep23.json
  - pubs-29aug25-sep23.json

Writes:
  - merged_publications_unique.json

Heuristics (in order):
 1) match normalized DOI
 2) match normalized URL
 3) match normalized title + first author last name + year
 4) optionally: fuzzy title matching (SequenceMatcher) with same year or same first author
When two items are considered duplicates, the script keeps the more "complete" record (higher score)
and fills missing fields from the other.
"""
import json
import re
import unicodedata
from difflib import SequenceMatcher
from collections import OrderedDict

IN_FILES = ["dart-publications-sep23.json", "pubs-29aug25-sep23.json"]
OUT_FILE = "merged_publications_unique.json"

# Set to True to attempt fuzzy title merges (can be slow for very large libraries)
FUZZY_MERGE = True
FUZZY_TITLE_THRESHOLD = 0.93  # 0.93 is strict; lower to be more aggressive (e.g. 0.90)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_items(data):
    """Return a list of item dicts given various possible JSON shapes."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # Common wrapper keys
        for k in ("items", "data", "records", "children", "entries"):
            if k in data and isinstance(data[k], list):
                return data[k]
        # sometimes a dict of id -> item:
        if all(isinstance(v, dict) for v in data.values()):
            return list(data.values())
    raise ValueError("Unsupported JSON structure: expected list or dict-of-items.")

def normalize_text(s):
    if not s:
        return ""
    s = str(s)
    s = unicodedata.normalize("NFKD", s)
    s = s.casefold()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^\w\s]", "", s)  # remove punctuation
    s = s.strip()
    return s

def normalize_doi(s):
    if not s:
        return ""
    s = str(s).strip().lower()
    s = re.sub(r"^doi:\s*", "", s)
    s = re.sub(r"^https?://(dx\.)?doi\.org/", "", s)
    s = s.strip()
    return s

def get_field(item, *names):
    """Return the first non-empty field value for any name in names (case-insensitive)."""
    lower_map = {k.lower(): k for k in item.keys()}
    for name in names:
        if name in item and item[name]:
            return item[name]
        ln = name.lower()
        if ln in lower_map:
            k = lower_map[ln]
            if item.get(k):
                return item[k]
    return None

def first_author_last(item):
    # Try typical creator/author keys
    for key in ("creators", "authors", "author", "creator", "contributors"):
        val = get_field(item, key)
        if not val:
            continue
        if isinstance(val, list) and val:
            a = val[0]
            # try different name fields
            for nm in ("family", "lastName", "last", "familyName", "surname"):
                if isinstance(a, dict) and a.get(nm):
                    return normalize_text(a.get(nm))
            # sometimes single string 'name'
            if isinstance(a, dict) and a.get("name"):
                nm = a.get("name")
                if "," in nm:
                    return normalize_text(nm.split(",")[0])
                return normalize_text(nm.split()[-1])
            if isinstance(a, str):
                if "," in a:
                    return normalize_text(a.split(",")[0])
                return normalize_text(a.split()[-1])
    return ""

def year_from_item(item):
    # try common date/year fields
    for key in ("year", "date", "issued", "issuedDate", "dateIssued", "publicationYear"):
        v = get_field(item, key)
        if not v:
            continue
        if isinstance(v, dict):
            # CSL JSON uses {'date-parts': [[YYYY,MM,DD]]}
            dp = v.get("date-parts") or v.get("date_parts")
            if isinstance(dp, list) and dp and isinstance(dp[0], list) and dp[0]:
                return str(dp[0][0])
        # try to find a 4-digit year
        m = re.search(r"\b(19|20)\d{2}\b", str(v))
        if m:
            return m.group(0)
    return ""

def score_item(item):
    """Simple completeness score: higher => more complete/preferable."""
    s = 0
    if normalize_doi(get_field(item, "DOI", "doi")):
        s += 50
    if get_field(item, "url", "URL"):
        s += 20
    if get_field(item, "abstract", "abstractNote", "notes"):
        s += 10
    for k in ("title", "publisher", "publicationTitle", "journal", "pages", "volume", "issue"):
        if get_field(item, k):
            s += 2
    # count authors/creators
    a = get_field(item, "creators", "authors", "author")
    if isinstance(a, list):
        s += min(10, len(a))
    return s

def merge_records(preferred, other):
    """Return a merged record: start from preferred, fill missing fields from other.
       For list fields, union them (preserve order)."""
    out = dict(preferred)  # copy
    for k, v in other.items():
        if k not in out or not out.get(k):
            out[k] = v
        else:
            # if both lists, make union
            if isinstance(out.get(k), list) and isinstance(v, list):
                # preserve existing order + append missing
                seen = set(json.dumps(x, sort_keys=True) if isinstance(x, dict) else str(x) for x in out[k])
                for elem in v:
                    key = json.dumps(elem, sort_keys=True) if isinstance(elem, dict) else str(elem)
                    if key not in seen:
                        out[k].append(elem)
                        seen.add(key)
            # if both strings but different, keep preferred (but do not lose the other)
            # (optionally could concatenate, but that sometimes corrupts fields)
    return out

def build_key_candidates(item):
    """Return a list of candidate keys for matching, in priority order."""
    keys = []
    doi = normalize_doi(get_field(item, "DOI", "doi") or "")
    if doi:
        keys.append("doi:" + doi)
    url = get_field(item, "url", "URL") or ""
    if url:
        keys.append("url:" + normalize_text(url))
    title = normalize_text(get_field(item, "title", "Title") or "")
    author = first_author_last(item)
    year = year_from_item(item)
    comp = f"title:{title}|author:{author}|year:{year}"
    keys.append(comp)
    # also title-only key
    keys.append("title:" + title)
    return [k for k in keys if k]

def main():
    all_items = []
    for p in IN_FILES:
        try:
            raw = load_json(p)
        except Exception as e:
            print(f"Error reading {p}: {e}")
            continue
        try:
            items = extract_items(raw)
        except ValueError:
            # fallback: if root is dict with key 'items'
            print(f"Warning: unrecognized structure in {p}, trying to coerce to list...")
            if isinstance(raw, dict):
                items = list(raw.values())
            else:
                raise
        print(f"Loaded {len(items)} items from {p}")
        all_items.extend(items)

    total_in = len(all_items)
    # Primary pass: build map by high-priority keys
    seen = {}  # key -> item
    key_to_primary = {}  # maps used key to canonical key (so doi:key and url:key both map)
    for item in all_items:
        candidates = build_key_candidates(item)
        matched = None
        for c in candidates:
            if c in seen:
                matched = c
                break
        if matched:
            existing = seen[matched]
            # choose the better record, but merge missing fields
            if score_item(item) > score_item(existing):
                merged = merge_records(item, existing)
                seen[matched] = merged
            else:
                merged = merge_records(existing, item)
                seen[matched] = merged
        else:
            # create an entry using the top candidate as canonical key
            canonical = candidates[0]
            seen[canonical] = item

    print(f"After heuristic dedup pass: {len(seen)} unique keys (from {total_in} total items).")

    # Optional fuzzy merge across title-similar items (expensive if many items)
    if FUZZY_MERGE:
        print("Running optional fuzzy-title merge pass (this may take a while for large lists)...")
        keys = list(seen.keys())
        items = [seen[k] for k in keys]
        used = [False] * len(items)
        merged_items = []

        for i in range(len(items)):
            if used[i]:
                continue
            base = items[i]
            base_title = normalize_text(get_field(base, "title") or "")
            base_author = first_author_last(base)
            base_year = year_from_item(base)
            j = i + 1
            while j < len(items):
                if used[j]:
                    j += 1
                    continue
                other = items[j]
                other_title = normalize_text(get_field(other, "title") or "")
                # only compare if both have titles
                if not base_title or not other_title:
                    j += 1
                    continue
                ratio = SequenceMatcher(None, base_title, other_title).ratio()
                other_author = first_author_last(other)
                other_year = year_from_item(other)
                # merge if title is very similar and (year or author matches or DOI missing)
                doi_base = normalize_doi(get_field(base, "DOI", "doi") or "")
                doi_other = normalize_doi(get_field(other, "DOI", "doi") or "")
                author_same = bool(base_author and other_author and base_author == other_author)
                year_same = bool(base_year and other_year and base_year == other_year)
                doi_same = bool(doi_base and doi_other and doi_base == doi_other)
                # conditions for fuzzy merge:
                if ratio >= FUZZY_TITLE_THRESHOLD and (author_same or year_same or (not doi_base and not doi_other)):
                    # decide which to prefer by score
                    if score_item(other) > score_item(base):
                        base = merge_records(other, base)
                    else:
                        base = merge_records(base, other)
                    used[j] = True
                j += 1
            merged_items.append(base)
            used[i] = True

        final_items = merged_items
        print(f"After fuzzy pass: {len(final_items)} unique items.")
    else:
        final_items = list(seen.values())

    # Write out
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_items, f, indent=2, ensure_ascii=False)

    print("Wrote", OUT_FILE)
    print(f"Input items: {total_in}, Output unique items: {len(final_items)}, Duplicates removed: {total_in - len(final_items)}")

if __name__ == "__main__":
    main()
