#!/usr/bin/python3.5

import pandas as pd
import numpy as np
from scipy.stats import norm, skewnorm

# Wrapper function for astoML's fit_bivariate_normal()
from fncs.fnc_fitGauss import fit2DnormalDistribution

# Extracts and returns actual inital particle source angles
from fncs.fnc_findSourceAngle import findSourceAngle

def calculateBulkAngle():
    theta_actual, phi_actual, numberOfParticles = findSourceAngle()

    det1 = pd.read_csv('./data/det1_hits.csv',
                           names=["x", "y", "z","energy"],
                           dtype={"x":np.float64,
                           "y": np.float64, "z":np.float64},
                           delimiter=',',
                           error_bad_lines=False,
                           engine='c')
    det2 = pd.read_csv('./data/det2_hits.csv',
                          names=["x", "y", "z","energy"],
                          dtype={"x":np.float64,
                          "y": np.float64, "z":np.float64},
                          delimiter=',',
                          error_bad_lines=False,
                          engine='c')

    ###########################
    ##### Bulk statistics #####
    ###########################

    # Maximum likelihood estimator
    x1_MLE, z1_MLE = np.median(det1['x']) , np.median(det1['z'])
    x2_MLE, z2_MLE = np.median(det2['x']) , np.median(det2['z'])

    # Standard Deviation
    std_dev_x1 = np.std(det1['x'])
    std_dev_z1 = np.std(det1['z'])
    std_dev_x2 = np.std(det2['x'])
    std_dev_z2 = np.std(det2['z'])


    # In [cm]
    delta_x = x2_MLE - x1_MLE
    delta_z = z2_MLE - z1_MLE

    gapBetweenDetectors = 0.51 # [cm]

    # Trig to experimentally back out initial angle
    theta_exp = round(np.rad2deg(np.arctan2(delta_z, gapBetweenDetectors)), 4)
    phi_exp = round(np.rad2deg(np.arctan2(delta_x, gapBetweenDetectors)), 4)


    with open('./data/results.txt', 'a') as f:
        f.write(str(numberOfParticles) +
        ',' + str(theta_actual) + ',' + str(phi_actual) +
        ',' + str(round(theta_exp, 4)) + ',' + str(round(phi_exp, 4)) +
        ',' + str(round(std_dev_z2, 4)) + ',' + str(round(std_dev_x2, 4)) + '\n')
