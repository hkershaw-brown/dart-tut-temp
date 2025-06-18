---
title: "Predicting Floods and Protecting Lives"
date: 2021-01-01T14:58:06-07:00
type: research
image: "images/science_nuggets/ats_local_200_1_teaser.webp"
hero: "images/hero/wrf-hydro.webp"
category: ["FLOOD PREDICTION"]
weight: 30
figures:
 - image : "/images/science_nuggets/ats_local_200_1.webp"
   caption : "A depiction of the along-the-stream localization scheme implemented in the project. The asterisks depict stream flow gauges and the rainbow-colored segments depict the specific areas affected by the assimilated data."
 - image : "/images/science_nuggets/pee_dee_hydrograph.webp"
   caption : "Precipitation and estimated stream flow for a hydrograph along the Pee Dee River. The Open Loop (orange line) refers to the estimated stream flow without data assimilation. The Prior (black line) and Posterior (dashed blue line) Means show significant reduction in the root mean squared error (RMSE)."
 - image : "/images/science_nuggets/fig_system_schematic.webp"
   caption : "A schematic depicting the data assimilation system used in the experiment."
---

Hurricanes are among the deadliest weather phenomena on earth. Hurricane
damages are usually associated with strong winds and other related impacts,
including storm surge, rainfall-induced floods and tornadoes.

Hurricane intensity is often categorized using the Saffir-Simpson
Hurricane Wind Scale, which ranges between 1 and 5. Hurricane Florence, a
category 4 hurricane, hit the Carolinas in September 2018 and caused
major flooding in coastal communities leading to 51 fatalities and damage
estimates of around $25 billion. According the National Weather Service,
certain locations in NC recorded over 30 inches of rain, exceeding the highest
single-storm rainfall amounts ever seen in the state.

Given this extreme threat to human life, predicting major floods due to
torrential rain is an urgent necessity. This, however, remains a challenge
given the short time-scale of flooding combined with multiple uncertainties
that limit the predictive capability of our water models. To tackle this,
scientists in the Data Assimilation Research Section (DAReS), in collaboration
with scientists in NCAR's Research Application Lab (RAL) and the University of
Texas at Arlington (UT Arlington) have recently developed a state-of-the-art
ensemble prediction system that aims to increase the accuracy of flood
forecasting during a hurricane landfall. The team coupled WRF-Hydro (the
research compartment of the National Water Model; Gochis et al. 2020) with the
Data Assimilation Research Testbed (DART; Anderson et al. 2009) and assimilated
hourly streamflow data, collected from a hundred United States Geological
Survey (USGS) gauges in the affected region. The framework uses 80 different
streamflow realizations, incorporating multiphysics uncertainty and
time-varying uncertainty in the forcing fluxes. The team also developed two
novel data assimilation techniques that helped improve the prediction accuracy
of the flood; namely, along-the-stream (ATS) localization and adaptive
covariance inflation (Gharamti 2018). "ATS localization, which is a
topologically-based updating scheme, helped reduce sampling errors for ungauged
basins at specific sites such as the Rocky River near Norwood, NC" describes
Dr. Gharamti from the DAReS team. He further adds "Adaptive inflation, on the
other hand, was extremely useful at mitigating extreme model and boundary
biases particularly near Pee Dee River in SC." 

Dr. McCreight from RAL really enjoyed the collaborative environment of this
work adding "Having weekly meetings where there is an opportunity to look and
investigate various hydrographs together, was indispensable for the success of
the projects." Concerning future plans, Dr. Gharamti said "Despite the success
of this work, looking ahead we plan to further improve the assimilation
framework by adding nonlinear streamflow updates that respect the non-Gaussian
(positive) nature of the variable. This can be done by a statistical
transformation, commonly referred to as Gaussian Anamorphosis."

The team submitted their research to Hydrology and Earth System Sciences, a
publication of the European Geophysical Union, where it is currently in review.
The project was led by Moha Gharamti (DAReS) and James McCreight (RAL) and
included contributions from Arezoo RafieeiNasab (RAL), Seong Jin Noh
(UT-Arlington; now at Kumoh National Institute of Technology in South Korea),
Tim Hoar (DAReS) and Ben Johnson (DAReS).

For more information, contact [Moha El Gharamti](https://staff.ucar.edu/users/gharamti) 
by emailing gharamti@ucar.edu.

### References

- Anderson, J., Hoar, T., Raeder, K., Liu, H., Collins, N., Torn, R., and Avellano, A.: The data assimilation research testbed: A community facility, *Bulletin of the American Meteorological Society*, **90**, 1283–1296, 2009.

- Gharamti, M.: Enhanced adaptive inﬂation algorithm for ensemble ﬁlters, *Monthly Weather Review*, **146**, 623–640, 2018.

- Gochis, D., Barlage, M., Cabell, R., Dugger, A., Fanfarillo, A., FitzGerald, K., McAllister, M., McCreight, J., RaﬁeeiNasab, A., Read, L., Frazier, N., Johnson, D., Mattern, J. D., Karsten, L., Mills, T. J., and Fersch, B.: *WRF-Hydro® v5.1.1*, [doi.org/10.5281/zenodo.3625238](https://doi.org/10.5281/zenodo.3625238), 2020.


