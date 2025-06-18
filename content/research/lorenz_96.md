---
title: "The Lorenz '96 model"
date: 2021-02-21T15:08:08-07:00
type: research
image: "images/science_nuggets/L96GoodRankHistogram.webp"
category: [LOW ORDER MODELS]
weight: 50
---

The Lorenz '96 model is one of our favorite models. In our implementation, it is a 40-variable model that can be used to test inflation algorithms, the effects of localization schemes, the integrity of the DART installation itself, the state-space diagnostic routines; it is extensively used in the tutorial, _and_ can even be run as a standalone executable to test the MPI support on a machine.

The images show rank historams used for evaluation assimlation performance - one good, one bad.

{{< figure src="/images/science_nuggets/L96.webp" class="site-project-single-image" >}} 

The Lorenz '96 model is described in

- Lorenz, E. N., and K. A. Emanuel, 1998:  
Optimal sites for supplementary weather observations: Simulations with a small model.  
*J. Atmos. Sci.*, **55**, 399-414.
[10.1175/1520-0469(1998)055\<0399:OSFSWO\>2.0.CO;2](https://doi.org/10.1175/1520-0469(1998)055%3C0399:OSFSWO%3E2.0.CO;2)

