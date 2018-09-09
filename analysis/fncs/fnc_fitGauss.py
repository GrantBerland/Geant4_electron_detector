#!/usr/bin/python3.5

from pandas import read_csv
from numpy import float64, median, mean, std
from astroML.stats import fit_bivariate_normal
from scipy.stats import skew

import matplotlib.pyplot as plt

def fit2DnormalDistribution(detector, fitFlag):
    if detector == 1:
        pathName = "./data/hits_det1.csv"
    elif detector == 2:
        pathName = "./data/hits_det2.csv"

    detector1_hits = read_csv(pathName,
                                 names=["x", "y", "z","energy"],
                                 dtype=float64)

    # Hit data from detector
    X = detector1_hits["x"]
    Z = detector1_hits["z"]

    # Descriptive statistics
    skew_x_dim = skew(X)
    skew_z_dim = skew(Z)

    x_med = median(X)
    z_med = median(Z)


    


    med = [x_med, z_med]
    if fitFlag == 1:
        # Bivariate normal fit
        (mu_nr, sigmaX_nr,
             sigmaZ_nr, alpha_nr) = fit_bivariate_normal(X, Z, robust=True)
    elif fitFlag == 0:
         mu_x = mean(X)
         mu_z = mean(Z)

         sigmaX_nr = std(X)
         sigmaZ_nr = std(Z)

         alpha_nr = None
         mu_nr = [mu_x, mu_z]



    Gauss2D_dist = {'Mean': mu_nr, 'Median': med,
                    'Sigma X': sigmaX_nr,
                    'Sigma Z': sigmaZ_nr, 'Alpha': alpha_nr,
                    'Skew X': skew_x_dim, 'Skew Z': skew_z_dim}


    return Gauss2D_dist
