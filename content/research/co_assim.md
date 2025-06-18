---
title: "Assimliation of CO"
date: 2021-02-21T14:48:20-07:00
type: research
image: "images/science_nuggets/CMAQ_graphic_teaser.webp"
category: [ATMOSPHERIC CHEMISTRY]
weight: 80
---

> This project describes an integrated approach to modeling atmospheric
> chemistry with trace gas data assimilation. Specifically, we ran CMAQ
> from within DART to assimilate both synthetic and real observations of
> CO for the period of June 2001.

> Alexis Zubrow

{{< figure src="/images/science_nuggets/CMAQ_graphic_teaser.webp" class="site-project-single-image" >}} 
{{< figure src="/images/science_nuggets/CMAQ_graphic2.webp" class="site-project-single-image" >}} 

> Fractional bias between the mean of the ensembles with and without data assimilation and the original full CMAQ run.

An integrated approach to modeling atmospheric chemistry with
trace gas data assimilation is a relatively new focus of the
atmospheric chemistry modeling community. It is expected that
the predictive capability of CTMs can be significantly improved
by assimilating measurements of key trace gases from
satellite-based platforms and surface monitors. Ensemble
adjustment Kalman filter (EAKF) methods are simple to implement,
don't need adjoints and backward integration, and are capable of
handling non-Gaussian model errors. These factors have led to the
adoption of EAKF methods for weather and climate simulations.
Additionally, EAKF provides a measure of error resulting from
the assimilation.  We have combined EAKF data assimilation with
a single-tracer version of CMAQ. The Data Assimilation Research
Testbed (DART), developed by NCAR, was used to create an EAKF
enabled CMAQ for assimilating CO. DART provides a modular
environment that can integrate dynamical models with various
assimilation techniques. Specifically, we ran CMAQ in ensemble
adjustment Kalman filter mode to assimilate both synthetic and
real observations of CO for the period of June 2001.
We argue that it is a viable approach for further data assimilation
experiments and potentially for air quality forecasting.



- Zubrow, A., L. Chen and V. R. Kotamarthi, **2008**  
EAKF-CMAQ: Introduction and evaluation of a data assimilation for CMAQ 
based on the ensemble adjustment Kalman filter,  
_J. Geophys. Res._, **113**, D09302,
[doi:10.1029/2007JD009267](https://doi.org/10.1029/2007JD009267)


