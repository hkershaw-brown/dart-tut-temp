---
title: "Xueli Huo Researches the Remote Arctic"
date: 2025-05-12T14:00:00-07:00
type: research
image: "images/featured-articles/xueli-huo.jpg"
hero: "images/hero/foothills-of-the-brooks-range.jpg"
figures:
 - image : "images/featured-articles/xueli-huo.jpg"
   caption : "Xueli Huo stands in front of Green Mountain."

category: ["LAND SURFACE MODELING"]
weight: 1
---

The effects of climate change are felt disproportionately in the polar regions of the Earth, with
projections showing that temperature changes in these regions will be five times larger than in the
tropics.

Yet understanding the effects of these changes on plant life, and by extension, the global carbon
cycle can be extremely difficult, due to the remoteness and extreme conditions of the polar regions.

Xueli Huo, a postdoctoral researcher at the University of Utah, studies Arctic and Boreal forests by
synthesizing satellite data into the NSF NCAR Community Land Surface Model. Land surface models are
used to represent the terrestrial biosphere and are a vital component of Earth system models. They
are used to estimate fluxes of carbon, water and energy exchange between the land surface and other
components in Earth system models such as the atmosphere and ocean.

In the larger context of Earth Science, land surface models are a relatively nascent type of
geophysical model. Historically, the models developed at NSF NCAR were fluid dynamical models, based
on formulations of the Navier-Stokes equations governing the fluid flow of the atmosphere and the
ocean. But in the 1990s, the modeling community realized the importance of developing a
comprehensive model of the land surface that realistically represented processes such as the
seasonal evolution of vegetation, streamflow in rivers, subsurface flow of groundwater, and the
cycling of carbon.

While each of these processes can be studied in isolation, doing so can leave a budding scientist
yearning to engage in harder problems. "The work I did during my master's was basically groundwater
statistics, and it was not hard to publish many papers. I thought it too easy and wanted to engage
in more sophisticated and meaningful scientific research," said Huo.

Combining the major land surface processes into an all-encompassing model that can be used by
ambitious researchers required decades of collaboration by scientists in several countries, since,
unlike the atmosphere and ocean, the evolution of the land surface cannot simply be described by a
set of governing equations.

An international team of scientists combined features from three existing models:

- the NCAR Land Surface Model
- the Institute of Atmospheric Physics Land Surface Model developed by the Chinese Academy of
  Sciences, and 
- the Biosphere-Atmosphere Transfer Scheme

to create the Common Land Model, a precursor to what is now known as the NSF NCAR Community Land
Model (CLM).

Over the decades, CLM has developed into a system that is comprehensive and intricate. Broadly
speaking, the surface can be occupied by different land types, such as glaciers, lakes, cities,
vegetation and crops. The vertical structure of the surface can account for different soil types and
snow depths. And fourteen different types of natural vegetation  and sixty-eight different crops can
be specified, each with their own set of unique properties such as variations in height and root
depth, effect on atmospheric flow, absorption and reflection of light and rates of photosynthetic
activity. 

All of this functionality in the model is specified by sets of equations, replete with numerical
parameters that must be tuned in order for the model to behave realistically.

"My master's supervisor recommended me to a famous professor at a renowned university in Beijing,
and I began working on optimizing parameters in land surface models. That was the starting point for
me to enter the world of sophisticated science," said Huo.

She continued, "Parameter optimization, which was the focus of my entire PhD, is one effective
method for reducing model uncertainty by minimizing the uncertainty in model parameter values." 
After finishing her PhD, Huo looked to go beyond parameter optimization in her research, leading her
to a postdoctoral position at the University of Arizona, "At the end of my PhD, I was certain that I
wanted to explore other techniques to reduce model uncertainty. This included data assimilation,
which reduces uncertainty in model initialization, and model structure improvement, which reduces
uncertainty in model structure," said Huo.

While at the University of Arizona, Huo became a visiting scholar at NSF NCAR, embedded with the
Data Assimilation Research Section, which develops the Data Assimilation Research Testbed (DART).

Huo uses CLM in conjunction with DART in order to synthesize real-world observational data into the
model to test and validate the model's performance. "The postdoc project aligns perfectly with my
research goals. I learned about the uncertainty in land model initialization and how effective data
assimilation can mitigate it," said Huo.

Many graduate students are first taught how to use a geophysical model when getting their start in a
particular field of science. Assimilating real-world data into a given model is an advanced skill
that often requires learning techniques beyond those taught in a typical graduate student's course
of study.

DART_LAB is a set of instructional materials designed to teach new users the fundamentals of data
assimilation. "As a user of DART, I like DART_LAB the most because it allows me to play around with
different 'knobs' and better understand how and why each of them can remove biases in model
simulations and makes the assimilation perform better," said Huo.

In an article published in the Journal of Geophysical Research: Biogeosciences, Huo worked with a
team that used DART to assimilate two data sources into CLM to assess the model's fidelity in Alaska
and Western Canada. The first data source she assimilated was Leaf Area Index (LAI), or the ratio of
leaf area to ground surface area inferred from a remote sensing instrument, in this case the
Moderate Resolution Imaging Spectroradiometer. The second data source she assimilated was a machine
learning product that estimated aboveground biomass.

The experiment compared CLM's estimates of Gross Primary Productivity (GPP) — how much carbon is
photosynthesized per year in a given area — both with and without data assimilation. This
methodology allowed Huo's team to obtain a benchmark of the model's default behavior and compare it
against the model's behavior when independent observational data was used as a constraint. Huo's
team found that assimilating LAI and aboveground biomass removed biases in modeled LAI and
aboveground biomass and thus reduced the model estimate of GPP by 41%. However, the estimated GPP is
still higher compared to a widely accepted benchmark data for GPP.

That left the team with an intriguing question: Why could be done to further reduce the bias in this
estimated GPP, even though it has already been improved through data assimilation?

Recent research by Rogers et al. (2019) provided a clue. They found that the rates of photosynthesis
in Arctic regions are much lower than estimated by land surface models because such models don't
currently take into account how the efficiency of photosynthetic activity in plants in response to
solar irradiance is affected by cold temperatures.

By modifying the photosynthetic parameterization in the CLM to account for this temperature
dependence, Huo's team was able to further decrease the model bias significantly.

Huo continues her work in land surface modeling as a postdoc at the University of Utah, an
environment that provides ample inspiration for future research questions. One major question she
ponders is how land surface models can be enhanced to improve the accuracy of snow simulations over
high mountains in the Western US, benefiting GPP and runoff simulations in this region.

Globally, she wonders, "What are the trends of terrestrial carbon fluxes in the future? Especially
the net carbon fluxes from land as input to the atmosphere."

Addressing these questions will require international collaboration among a new generation of
scientists, akin to those who developed the current suite of land surface models a generation ago.
Huo will surely relish the opportunity to contribute.

### References

Huo, X., A. M. Fox, H. Dashti, C. Devine, W. Gallery, W. K. Smith, B. Raczka, J. L. Anderson,
A. Rogers, D. J. P. Moore, 2024: Integrating State Data Assimilation and Innovative Model
Parameterization Reduces Simulated Carbon Uptake in the Arctic and Boreal Region. *JGR Biosciences*, 
**129**, e2024JG008004, [doi.org/10.1029/2024JG008004](https://doi.org/10.1029/2024JG008004).

Rogers, A., S. P. Serbin, K. S. Ely, and S. D. Wullschleger, 2019: Terrestrial biosphere models may
overestimate Arctic CO2 assimilation if they do not account for decreased quantum yield and
convexity at low temperature. *New Phytologist*, **223**, 167–179,
[doi.org/10.1111/nph.15750](https://doi.org/10.1111/nph.15750).
