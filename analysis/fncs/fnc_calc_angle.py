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

    # Returns a dictionary with attributes 'Mean', Sigma X','Sigma Y','Alpha'
    # Fit flag 0: calculates statistics along X and Z axes
    # Fit flag 1: fits a 2D normal distribution to data and returns theoretical statistics
    det1 = fit2DnormalDistribution(detector=1, fitFlag=1)
    det2 = fit2DnormalDistribution(detector=2, fitFlag=1)


    # Determines what statistic is used to estimate the maximum likelihood point
    if stat == 'median':
        x1, z1 = det1['Median']
        x2, z2 = det2['Median']
    elif stat == 'mean':
        x1, z1 = det1['Mean']
        x2, z2 = det2['Mean']

    # Normal distribution rotation extraction
    alpha1 = det1['Alpha']
    alpha2 = det2['Alpha']

    # Skew extractions
    skew_x1 = det1['Skew X']
    skew_z1 = det1['Skew Z']

    skew_x2 = det2['Skew X']
    skew_z2 = det2['Skew Z']

    # Standard Deviation extractions
    std_dev_x1 = det1['Sigma X']
    std_dev_z1 = det1['Sigma Z']

    std_dev_x2 = det2['Sigma X']
    std_dev_z2 = det2['Sigma Z']


    # In [cm]
    delta_x = x2 - x1
    delta_z = z2 - z1


    gapBetweenDetectors = 0.52 # [cm]

    # Trig to experimentally back out initial angle
    theta_exp = round(np.rad2deg(np.arctan2(delta_z, gapBetweenDetectors)), 4)
    phi_exp = round(np.rad2deg(np.arctan2(delta_x, gapBetweenDetectors)), 4)

    # Computes absolute error between actual and experimental angle, since
    # the actual angle can be 0, which blows up traditional relative error
    theta_error = round(theta_exp - theta_actual, 4)
    phi_error = round(phi_exp - phi_actual, 4)

    with open('./data/results.txt', 'a') as f:
        f.write(str(numberOfParticles) +
        ',' + str(theta_actual) + ',' + str(phi_actual) +
        ',' + str(round(np.mean(theta), 4)) + ',' + str(round(np.std(theta), 4)) +
        ',' + str(round(np.mean(phi), 4)) + ',' + str(round(np.std(phi), 4)) +
        ',' + str(round(np.median(theta), 4)) + ',' + str(round(np.median(phi), 4)) +
        ',' + str(round(mu_theta, 4)) + ',' + str(round(std_theta, 4)) +
        ',' + str(round(mu_phi, 4)) + ',' + str(round(std_phi, 4)) +
        ',' + str(round(mean_t,4)) + ',' + str(round(sig_t,4)) +
        ',' + str(round(mean_p,4)) + ',' + str(round(sig_p,4)) + '\n')
