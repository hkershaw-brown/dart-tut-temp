---
title: "DART\_LAB"
date: 2020-01-24T13:36:06+06:00
image: images/tutorial/dart-lab-thumb.png
feature_image: images/tutorial/dart-lab.png
weight: 1
category: "MATLAB"
author: dart
summary: "A MATLAB®-based tutorial to demonstrate the principles of 
          ensemble data assimilation."
---
#### An introduction to Data Assimilation using MATLAB


DART\_LAB is a MATLAB®-based tutorial to demonstrate the principles of 
ensemble data assimilation.

This tutorial begins at a more introductory level
than the materials in the tutorial directory, and includes hands-on exercises
at several points. In a workshop setting, these materials and exercises took
about 1.5 days to complete.

DART\_LAB consists of PDF tutorial materials and MATLAB® exercises.
See below for links to the PDF files and a list of the 
corresponding MATLAB scripts.

#### DART\_LAB tutorial slides

[1. Ensemble Data Assimilation Concepts in 1D.](https://docs.dart.ucar.edu/en/latest/_downloads/7d7f7127807b27dc004fc495daa6c075/DART_LAB_Section01.pdf)

[2. How Should Observations Impact an Unobserved State Variable? Multivariate Assimilation.](https://docs.dart.ucar.edu/en/latest/_downloads/c41fccc195c1c0334ac0360b0add33fd/DART_LAB_Section02.pdf)

[3. Inflation and Localization to Improve Performance.](https://docs.dart.ucar.edu/en/latest/_downloads/f50386414b0cddd1fafce5a942240f42/DART_LAB_Section03.pdf)

[4. Nonlinear and Non-Gaussian Extensions.](https://docs.dart.ucar.edu/en/latest/_downloads/0b8f5ce742ddd403f16e4d5a15ce6b8a/DART_LAB_Section04.pdf)

[5. Adaptive Inflation.](https://docs.dart.ucar.edu/en/latest/_downloads/99efe1ee0df2c5453e390b56f59be784/DART_LAB_Section05.pdf)


#### Hands-on Exercises

The DART\_LAB materials are bundled with DART. 

You can download [DART](https://github.com/NCAR/DART) from Github using 

````
git clone https://github.com/NCAR/DART.git
````

In the `guide/DART_LAB/matlab` subdirectory are a set of MATLAB scripts and 
graphical user interface (GUI) programs which are exercises that go with the 
tutorial. Each is interactive with settings that can be changed and 
rerun to explore various options. A valid
[MATLAB](http://www.mathworks.com/products/matlab/)
license is needed to run these scripts.

The exercises use the following functions:

- `bounded_oned_ensemble`
- `gaussian_product`
- `oned_cycle`
- `oned_ensemble`
- `oned_model`
- `oned_model_inf`
- `run_lorenz_63`
- `run_lorenz_96`
- `run_lorenz_96_inf`
- `twod_ensemble`
- `twod_ppi_ensemble`

To run these, cd into the `DART_LAB/matlab` directory, start matlab, and type
the names at the prompt.
