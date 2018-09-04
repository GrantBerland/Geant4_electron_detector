#!/usr/bin/python3.5

from pandas import read_csv
from numpy import float64, median
from astroML.stats import fit_bivariate_normal
from scipy.stats import skew

import matplotlib.pyplot as plt

def fit2DnormalDistribution(detector):
    if detector == 1:
        pathName = "./data/hits_det1.csv"
    elif detector == 2:
        pathName = "./data/hits_det2.csv"

    detector1_hits = read_csv(pathName,
                                 names=["x", "y", "z"],
                                 dtype=float64)

    # Hit data from detector
    X = detector1_hits["x"]
    Z = detector1_hits["z"]

    (mu_nr, sigma1_nr,
         sigma2_nr, alpha_nr) = fit_bivariate_normal(X, Z, robust=True)

    skew_x_dim = skew(X)
    skew_z_dim = skew(Z)

    x_med = median(X)
    z_med = median(Z)

    Gauss2D_dist = {'Mean': mu_nr, 'Median X': x_med, 'Median Z': z_med,
                    'Sigma X': sigma1_nr,
                    'Sigma Z': sigma2_nr, 'Alpha': alpha_nr,
                    'Skew X': skew_x_dim, 'Skew Z': skew_z_dim}


    return Gauss2D_dist
