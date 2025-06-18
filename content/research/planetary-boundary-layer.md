---
title: "Planetary Boundary Layer"
date: 2021-02-21T15:03:37-07:00
type: research
image: "images/science_nuggets/JoshDorita_graphic_teaser.webp"
category: [PLANETARY BOUNDARY LAYER]
weight: 60
---

> A long-term goal of this work is to find an efficient system for probabilistic 
> planetary boundary layer (PBL) nowcasting that can be employed wherever 
> surface observations are present. One approach showing promise is the use 
> of a single column model (SCM) and ensemble filter data assimilation techniques.

> Dorita Rostkier-Edelstein  
> Josh Hacker

Hacker and Rostkier-Edelstein (2007) showed that surface observations can 
be an important source of information with an SCM and an ensemble filter.
Here we extend that work to quantify the probabilistic skill of the SCM with 
added complexity. Although it is appealing to add additional physics and dynamics 
to the SCM model it is not immediately clear that additional complexity will 
improve the performance of a PBL nowcasting system based on a simple model.
We address this question with regard to treatment of surface assimilation,
radiation in the column, and also advection to account for realistic 3D  
dynamics (a timely WRF prediction). We adopt a factor separation analysis 
to quantify the individual contribution of each model component to the 
probabilistic skill of the system, as well as any beneficial or detrimental 
interactions between the different factors.

The probabilistic skill of the system is evaluated through the Brier Skill Score (BSS)
and the area under the relative operating characteristic (ROC) curve (AUR). The BSS is
further decomposed into both a reliability and resolution term to understand the 
trade-offs in different components of probabilistic skill. These metrics verify 
events, and we define an event here to be a forecast value exceeding the 75th 
percentile. The climatology of the observations during the verification period 
was chosen as reference system.

{{< figure src="/images/science_nuggets/JoshDorita_graphic.webp" class="site-project-single-image" >}} 

> Figure 1: Brier (on 75th percentile observations) reliability term 
> (negative orientation) and area under the ROC (AUR; positively orientation) 
> for potential temperature profiles at night (75th percentile observations).
> Blackcurves: values skill of baseline system.
> Red curves: skill including the contribution of a given factor.
> Dashed curves are corresponding 95% confidence intervals.

Results show that assimilation of surface observations can improve skill more 
significantly than major model improvements. Figure 1 illustrates some of the 
probabilistic verification results for potential temperature profiles estimated at  
night (0530 UTC, 0030 LT). Black curves show the values of the metrics obtained 
for the baseline system. Red curves show the resulting values when the contribution 
of a given factor is included. Confidence intervals (thin dashed curves) were 
calculated using a bootstrapping technique. Brier reliability and discrimination 
are both significantly improved through the lowest few hundred meters when 
assimilation is used, but advection is not as successful.


- Hacker, J. P. and D. Rostkier-Edelstein, **2007**  
PBL state estimation with surface observations, a column model, and an ensemble filter.  
_Mon. Wea. Rev._, **135**, 2958-2972
[doi:10.1175/MWR3443.1](https://doi.org/10.1175/MWR3443.1)


