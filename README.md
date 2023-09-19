# FourierShellCorr
Python script to compute Fourier Shell Correlation curve between two half-3D density maps


## General description

Fourier Shell Correlation (FSC) is a gold-standard methodology which is used in cryo-EM field to estimate the resolution of cryo-EM maps.
FSC, originally proposed by Harauz and van Heel in 1986, is a generalization to three dimensions of two-dimensional Fourier Ring Correlation (FRC).<sup>1</sup>
As in the case of FRC, Fourier Shell Correlation analysis requires to divide data set into two independent subsets. In this particular example, FSC is computed between two half-3D density maps.
Half-maps were generated using interleaved frames (odd and even) of conformational ensemble (see repository [_3D_DensityMap_](https://github.com/mpopara/3D_DensityMap) for more details). 

Calculating correlation function in three-dimensional space is computationally demanding, since it requires to solve triple integrals. This is easily circumvented via the use of Fourier transforms,
since the Fourier transform of the correlation between two functions is equal to the simple product of their Fourier transforms.
Therefore, in the first step, half-3D density maps are Fourier transformed. Next, for each of the voxels in the density map, calculated is its distance to the center of density map. This allows us to define set of concentric shells, each of which
contains those voxels that fall within a given distance from the center.
Next, we loop over the shells, and perform a shell-to-shell correlation between the half-maps in the following manner: for each of the voxels in the shell, multiplied are Fourier transforms of half-maps, and subsequently this product is summed over all voxels in a shell and normalized.<sup>1</sup> 

At the end of the analysis, results are printed as a two-column txt file, where the first column contans the distance of each of the shells to the center of density map, and the second column contains the FSC value at a given shell. This result is also
visualized and saved as png and svg file, as illustrated below.

![FSC_mapname](https://github.com/mpopara/FourierShellCorr/assets/40856779/9cf53eea-acd4-49ab-8f5f-7ff1d1816d19)

Illustration of the FSC curve in this help file is adapted from Dittrich _et al_, 2023.<sup>2</sup> 

Precision of a full 3D density maps is assigned to a point at which the FSC curve intersects horizontal dashed line at the FSC = 0.143, i.e. 1/7. In this example, it was found that precision of full 3D density map is 9.8 Å. However, note that the
precision of the individual structures in the ensemble can be much lower than that.
Choice of FSC threshold at which the precision (or resolution) is estimated, is a topic of ongoing discussions, and several alternative criteria are proposed, such as 0.5 threshold, information criteria and &sigma;-factor criterion.<sup>3</sup>

## Input file requirements

For the computation of FSC required are:

* two half-maps in .mrc file format (see repository[_3D_DensityMap_](https://github.com/mpopara/3D_DensityMap) for details on how to compute half maps)


## Dependencies
_compute_fsc.py_ is a python script which was tested with provided [exemplary data](https://github.com/mpopara/FourierShellCorr/tree/main/example_data) under the following configuration:

* Windows Subsystem Linux (WSL) Ubuntu 18.04.5
* Python 3.7.10
* emda 1.1.4 (which in turn requires: numpy, pandas, scipy, gemmi, servalcat, mrcfile, matplotlib)


## References
1. Harauz, G. and van Heel, M. (1986) Exact Filters for General Geometry Three Dimensional Reconstruction. Optik, 73, 146-156. 

2.   Dittrich, J.; Popara, M.; Kubiak, J.; Dimura, M.; Schepers, B.; Verma, N.; Schmitz, B.; Dollinger, . P.; Kovacic, F.; Jaeger, K. E.;
Seidel, C. A. M.; Peulen, T. O.; Gohlke, H., Resolution of Maximum Entropy Method-Derived Posterior Conformational Ensembles of a Flexible System Probed by FRET and Molecular Dynamics Simulations.
J Chem Theory Comput 2023, 19 (8), 2389-2409.

3. M. Van Heel, M. Schatz, Fourier shell correlation threshold criteria. J. Struct. Biol., 151 (2005), pp. 250-262,

## Authors

* Milana Popara
* Thomas-Otavio Peulen
