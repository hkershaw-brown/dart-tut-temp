---
title: "Model for Prediction across Scales"
weight: 10
date: 2019-12-23T15:44:46+06:00
type: research
image: "images/science_nuggets/mpas_teaser.webp"
category: ["WEATHER PREDICTION"]
---

Data assimilation for MPAS is available as an ensemble Kalman filter (EnKF)
implemented through [Data Assimilation Research Testbed](http://dart.ucar.edu)

This work is done in a collaborative effort between the
[Mesoscale and Microscale Meteorology (MMM)](http://www.mmm.ucar.edu)
Division and the DART development team. DART support for both MPAS-Atmosphere
and MPAS-Ocean are available as part of the standard DART package.

In collaboration with NOAA's [Earth System Research Laboratory](http://www.esrl.noaa.gov)
related efforts are also underway to explore ensemble data assimilation
for MPAS-Atmosphere with the
Gridpoint Statistical Interpolation (GSI) scheme that is operational at
[the National Centers for Environmental Prediction](http://www.ncep.noaa.gov).

{{< figure src="/images/science_nuggets/MPAS_spaghetti_Z500mb_anal.2008090512.webp" class="site-project-single-image" >}} 

Grid structure used in the MPAS/DART interface
The MPAS/DART interface is
built on MPAS's unstructured centroidal Voronoi mesh,
and does not regrid to latitude-longitude grids. In MPAS, the finite-volume
approach based on a C-grid staggering retains prognostic equations for mass
at the center of finite-volume cells and for the normal component of velocity
_(u)_ at the faces (or edges in 2D) of the cells.
The normal component of velocity _(u)_ at cell edges is then used to
reconstruct zonal and meridional winds at cell centers _(V)_
 using radial basis functions (RBFs).
To avoid the singularity issue on the poles, the cartesian coordinate is employed.

{{< figure src="/images/science_nuggets/MPAS_grid_components.webp" class="site-project-single-image" >}} 

The forward operators on the unstructured grid mesh are constructed as follows.
The dual of the Voronoi mesh, or the triangular mesh (shown as dashed lines in the
figure), is used to search the closest cell center to an arbitrary (or observation)
point, then find three cell centers of the triangle enclosing the desired point.
Mass fields are then horizontally interpolated from the cell centers to the observation
location using a barycentric (e.g., area-weighted) interpolation.

While the observed wind quantities are zonal and meridional winds, the normal
component of velocity _(u)_ is the only prognostic wind variable in MPAS,
we thus implement a couple of different ways of assimilating wind observations.
The options determine which wind variables are used in the forward operator to
compute expected observation values; how the horizontal interpolation is computed
in that forward operator; and how the assimilation increments are applied to update
the wind quantities in the state vector of the analysis.

Preliminary results based on real data assimilation experiments indicate that
performance is better when the zonal and meridional winds are used as input to the
forward operator that uses Barycentric interpolation and the prognostic _(u)_
wind is incrementally updated. However, there remain scientific questions about
how best to handle the wind fields under different situations.

For any questions or future collaboration, please contact either
Soyoung Ha (syha@ucar.edu) or the DART team (dart@ucar.edu)

- Ha, S., C. Snyder, W. C. Skamarock, J. Anderson and N. Collins, **2017**
Ensemble Kalman filter data assimilation for the Model for Prediction
Across Scales (MPAS).
_Monthly Weather Review_, **145**, 4673-4692,
[doi:10.1175/MWR-D-17-0145.1](https://doi.org/10.1175/MWR-D-17-0145.1)

