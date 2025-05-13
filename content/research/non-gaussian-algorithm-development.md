---
title: "Ian Grooms and Novel Algorithm Development"
date: 2025-05-11T14:00:00-07:00
type: research
image: "images/featured-articles/ian-grooms.jpg"
hero: "images/hero/growth-on-wall.jpg"
figures:
 - image : "images/featured-articles/ian-grooms.jpg"
   caption : "Ian Grooms in an atrium at the University of Colorado's Engineering Center."

category: ["COMMUNITY CONTRIBUTIONS TO DART"]
weight: 1
---

Ensemble data assimilation algorithms, such as those implemented in the Data
Assimilation Research Testbed (DART), can trace their lineage to the Kalman
filter (Kalman, 1960) which was developed for aerospace applications in the
1960’s. The Kalman filter uses a single mathematical model to represent how the
state of the dynamical system evolves over time and a covariance matrix to
represent the uncertainty in the estimation of the system’s state. Measurements
from sensors, which inherently contain errors, are incorporated in a manner
that minimizes mean squared error of the estimated state, given a linear model
and Gaussian errors. The Kalman Filter was used to estimate the trajectory of
spacecraft using measurements from onboard sensors and was incorporated into
the guidance system for the Apollo program, helping NASA astronauts
successfully land on the moon and return home safely. 

Decades later, in 1990's and early 2000's, scientists began adapting Kalman's
idea for use in the context of geophysical fluid dynamics. Instead of using a
covariance matrix to represent the uncertainty in the state estimate, an
ensemble of geophysical models is used, giving rise to assimilation
methodologies such as the Ensemble Kalman Filter and Ensemble Adjustment Kalman
Filter (Evensen, 1994; Houtekamer & Mitchell, 1998; Burgers et al., 1998;
Anderson, 2003). The formulation of these early approaches assumes that the
underlying probability distributions that characterize both the model
uncertainty and observation errors are Gaussian. 

In many geophysical applications this assumption of Gaussianity degrades the
ability of such filters to provide a skillful state estimate. Examples of
non-Gaussianity include ensemble forecasts where some ensemble members have
cloudy conditions and other members have clear conditions, with few or no
members in between (Chan et al., 2023). Ensemble forecasts of rain rates are
also non-Gaussian because a Gaussian distribution would imply a positive
probability of negative rain, and algorithms based on Gaussian assumptions can
produce ensemble members with negative rain rates. Similarly, Gaussian
distributions are not appropriate for quantities like concentrations, which
must remain between 0 and 100%.

Ian Grooms, Associate Professor of Applied Mathematics at the University of
Colorado at Boulder, studies such problems in the course of his research in
geophysical fluid dynamics and data assimilation. Grooms (2022) reviews
techniques used to broaden the applicability of the Ensemble Kalman Filter to
quantities in nature that exhibit non-Gaussian behavior and discusses how the
assumption of Gaussianity is not essential for the implementation of ensemble
data assimilation algorithms. In particular, the two-step implementation (in
which the first step produces an improved estimate of the observed quantity,
and the second step updates the model variables conditionally on the updated
observed variables) of many ensemble algorithms allows for the use of advanced
techniques to represent non-Gaussian probability distributions of the model
uncertainty and observation errors.

In Grooms and Riedel (2024), the authors develop a novel two-step algorithm,
named the Kernel-based Quantile-Conserving Ensemble Filter (KQCEF), for
assimilating sea ice concentration. Sea ice concentration is the fraction of
area in a given region that is covered by sea ice, and is thus between 0 and
100%. “Sea ice data assimilation is a particularly difficult problem because of
its decidedly non-Gaussian character, and I'm grateful to my colleagues for
introducing me to it. I developed the KQCEF in the context of sea ice data
assimilation, but I hope that it will prove useful for other problems with
similar characteristics.” said Grooms.

As an applied mathematician, Grooms finds that having a particular problem in
mind can motivate the development of new techniques. “I'm interested in
developing methods with wide applicability, but I've decided to try to move
from the particular to the universal rather than vice versa. That way, if I
make progress on one particular problem, it has value even if the progress
doesn't extend to other problems,” said Grooms.

Beyond publishing his results, Grooms implemented the KQCEF in DART so it can
be shared with other members of the research community. DART is an open-source
repository for ensemble data assimilation developed and maintained by staff at
the NSF National Center for Atmospheric Research (NSF NCAR).

NSF NCAR is managed by the University Corporation for Atmospheric Research, a
non-profit entity overseen by a consortium of over 130 North American colleges
and universities, providing a governance structure that helps to ensure that
software developed by NSF NCAR staff meets the needs of researchers in the
university community. “A lot of fundamental research on data assimilation
methods happens at universities,” said Grooms. “Because of the prohibitive
costs of setting up from scratch systems that are close to real-world data
assimilation, if it were not for projects like DART many university research
groups in data assimilation would confine their research to toy models and
sketches of real problems, or would spend all their time on the software with
little time left for theory.”

Scaling computational capability of a data assimilation system up from a toy
model to a realistic geophysical model can take years of development effort.
Grooms continued, “DART is an example of how an open-source project, led by a
team of experts at a government-funded research center who devote time and
resources towards enabling community involvement, can bridge the gap between
theory and practice, bringing cutting-edge research to operational systems,
and opening the black box of operational software to university researchers.”

Feedback from faculty and students often helps to directly guide developments
in DART. “Graduate students are motivated and capable, and many continue to
learn and use DART. That said, in my experience many beginning students are
primarily familiar with Python, and don't have a lot of experience with Bash
scripting, let alone Fortran. A Python interface to configure, run, and then
explore the output of experiments using the toy models already incorporated in
DART might help get students started,” said Grooms.

In response to such feedback, a notable recent addition is the creation of a
python-based diagnostics package for DART output, known as
[pyDARTdiags](https://github.com/NCAR/pyDARTdiags). The package uses scientific
python libraries that many students are familiar with such as numpy, pandas and
plotly to display observation space diagnostics in interactive Jupyter
notebooks. 

Going forward, Grooms sees more possibilities for novel data assimilation
applications. He continued, “I'm currently developing two-step updates further
in the context of sea ice data assimilation, extending beyond concentration to
thickness observations, and to sophisticated methods for dealing with the ice
thickness distributions and floe size distributions. Looking ahead, I'm
interested in using two-step updates for parameter estimation in Earth system
models, and I'm also looking for new challenging problems where non-Gaussian
methods can have an impact.”

### References

Anderson, J. L., 2003: A Local Least Squares Framework for Ensemble Filtering.
*Monthly Weather Review*, **131**, 634–642, [https://doi.org/10.1175/1520-0493(2003)131<0634:ALLSFF>2.0.CO;2](https://doi.org/10.1175/1520-0493\(2003\)131\<0634:ALLSFF\>2.0.CO;2).

Burgers, G., P. J. van Leeuwen, and G. Evensen, 1998: Analysis Scheme in the
Ensemble Kalman Filter. *Monthly Weather Review*, **126**, 1719–1724, [https://doi.org/10.1175/1520-0493(1998)126<1719:ASITEK>2.0.CO;2](https://doi.org/10.1175/1520-0493\(1998\)126\<1719:ASITEK\>2.0.CO;2).

Chan, M.-Y., X. Chen, and J. L. Anderson, 2023: The Potential Benefits of Handling Mixture Statistics via a Bi-Gaussian EnKF: Tests With All-Sky Satellite Infrared Radiances. *Journal of Advances in Modeling Earth Systems, **15**, e2022MS003357, [https://doi.org/10.1029/2022MS003357](https://doi.org/10.1029/2022MS003357).

Evensen, G., 1994: Sequential data assimilation with a nonlinear quasi-geostrophic model using Monte Carlo methods to forecast error statistics. *Journal of Geophysical Research: Oceans*, **99**, 10143–10162, [https://doi.org/10.1029/94JC00572](https://doi.org/10.1029/94JC00572).

Grooms, I., 2022: A comparison of nonlinear extensions to the ensemble Kalman
filter. *Computational Geosciences*, **26**, 633–650, [https://doi.org/10.1007/s10596-022-10141-x](https://doi.org/10.1007/s10596-022-10141-x).

Grooms, I., and C. Riedel, 2024: A Quantile-Conserving Ensemble Filter Based on
Kernel-Density Estimation. *Remote Sensing*, **16**, 2377, [https://doi.org/10.3390/rs16132377](https://doi.org/10.3390/rs16132377).

Houtekamer, P. L., and H. L. Mitchell, 1998: Data Assimilation Using an Ensemble Kalman Filter Technique. *Monthly Weather Review*, **126**, 796–811, [https://doi.org/10.1175/1520-0493(1998)126<0796:DAUAEK>2.0.CO;2](https://doi.org/10.1175/1520-0493\(1998\)126\<0796:DAUAEK\>2.0.CO;2).

Kalman, R. E., 1960: A New Approach to Linear Filtering and Prediction Problems. *Journal of Basic Engineering*, **82**, 35–45, [https://doi.org/10.1115/1.3662552](https://doi.org/10.1115/1.3662552).
