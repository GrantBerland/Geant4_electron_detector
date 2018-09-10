#!/usr/bin/python3.5

import pandas as pd
import numpy as np
from astroML.stats import fit_bivariate_normal
from scipy.stats import skew


def fit2DnormalDistribution(detector, fitFlag):

    detector_hits = pd.read_csv('./data/hits.csv',
                                 names=["det","x", "y", "z","energy", "code"],
                                 dtype={"det": np.int32, "x":np.float64,
                                        "y": np.float64, "z":np.float64,
                                         "code": np.unicode_})



    # Hit data from detector
    whichDetectorIndex = detector_hits.index[(detector_hits["det"] == detector)
                                             & (detector_hits["code"] == "GH")].tolist()


    X = detector_hits["x"][whichDetectorIndex]
    Z = detector_hits["z"][whichDetectorIndex]

    # Descriptive statistics
    skew_x_dim = skew(X)
    skew_z_dim = skew(Z)

    med = [np.median(X), np.median(Z)]


    if fitFlag == 1:
        # Bivariate normal fit
        (mu_nr, sigmaX_nr,
             sigmaZ_nr, alpha_nr) = fit_bivariate_normal(X, Z, robust=True)
    elif fitFlag == 0:

         sigmaX_nr = np.std(X)
         sigmaZ_nr = np.std(Z)

         alpha_nr = None
         mu_nr = [np.mean(X), np.mean(Z)]



    Gauss2D_dist = {'Mean': mu_nr, 'Median': med,
                    'Sigma X': sigmaX_nr,
                    'Sigma Z': sigmaZ_nr, 'Alpha': alpha_nr,
                    'Skew X': skew_x_dim, 'Skew Z': skew_z_dim}


    return Gauss2D_dist
