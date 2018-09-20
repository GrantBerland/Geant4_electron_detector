#!/usr/bin/python3.5


import pandas as pd
import numpy as np

from scipy.stats import norm, skewnorm

# Extracts and returns actual inital particle source angles
from .fnc_findSourceAngle import findSourceAngle

def calculateAnglePerParticle():
    detector_hits = pd.read_csv('./data/hits.csv',
                               names=["det","x", "y", "z","energy", "code"],
                               dtype={"det": np.int8, "x":np.float64,
                               "y": np.float64, "z":np.float64,
                               "code": np.unicode_},
                               delimiter=',',
                               error_bad_lines=False,
                               skiprows=1,
                               engine='c')


    detectorDoubleHits = detector_hits.index[detector_hits["code"] == "DH"].tolist()

    whichDetectorIndex = detector_hits.index[detector_hits["code"] == "GH"].tolist()

    [det, X, Z]  = [detector_hits['det'][whichDetectorIndex],
                   detector_hits['x'][whichDetectorIndex],
                   detector_hits['z'][whichDetectorIndex]]


    deltaX = np.zeros(len(det), dtype=np.float64)
    deltaZ = np.zeros(len(det), dtype=np.float64)

    gap = 0.52 # cm

    array_counter = 0
    for count, el in enumerate(det):
        # pandas series can throw a KeyError if character starts line
        # TODO: replace this with parse command that doesn't import keyerror throwing lines
        while True:
            try:
                pos1 = det[count]
                pos2 = det[count+1]

                X[count]
                Z[count]

                X[count+1]
                Z[count+1]
            except KeyError:
                count = count + 1
                if count == len(det):
                    break
                continue
            break

        # Checks if first hit detector == 1 and second hit detector == 2
        if np.equal(pos1, 1) & np.equal(pos2, 2):
            deltaX[array_counter] = X[count+1] - X[count]
            deltaZ[array_counter] = Z[count+1] - Z[count]

            # Successful pair, continues to next possible pair
            count = count + 2
            array_counter = array_counter + 1
        else:
            # Unsuccessful pair, continues
            count = count + 1

    # Remove trailing zeros
    deltaX_rm = deltaX[:array_counter]
    deltaZ_rm = deltaZ[:array_counter]

    del deltaX
    del deltaZ

    # Find angles in degrees
    theta = np.arctan2(deltaZ_rm, gap) * 180 / np.pi
    phi = np.arctan2(deltaX_rm, gap) * 180 / np.pi

    # Fit a standard normal distribution to data
    try:
        x_theta = np.linspace(min(theta), max(theta))
        mu_theta, std_theta = norm.fit(theta)
        p_theta = norm.pdf(x_theta, mu_theta, std_theta)

        x_phi = np.linspace(min(phi), max(phi))
        mu_phi, std_phi = norm.fit(phi)
        p_phi = norm.pdf(x_phi, mu_phi, std_phi)

    except:
        pass
    # Fit skew normal distribution to data
    mean_t, var_t, skew_t = skewnorm.fit(theta)
    mean_p, var_p, skew_p = skewnorm.fit(phi)


    theta_actual, phi_actual, numberOfParticles = findSourceAngle()

    with open('./data/results.txt', 'a') as f:
        f.write(str(numberOfParticles) +
        ',' + str(theta_actual) + ',' + str(phi_actual) +
        ',' + str(round(np.mean(theta), 4)) + ',' + str(round(np.std(theta), 4)) +
        ',' + str(round(np.mean(phi), 4)) + ',' + str(round(np.std(phi), 4)) +
        ',' + str(round(np.median(theta), 4)) + ',' + str(round(np.median(phi), 4)) +
        ',' + str(round(mu_theta, 4)) + ',' + str(round(std_theta, 4)) +
        ',' + str(round(mu_phi, 4)) + ',' + str(round(std_phi, 4)) + '\n')
