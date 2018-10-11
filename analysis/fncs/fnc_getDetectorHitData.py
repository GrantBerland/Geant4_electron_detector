#!/usr/bin/python3.5


import pandas as pd
import numpy as np


def getDetectorHitData(detector):
    if detector == 1:
        fileName = './data/det1_hits.csv'
    elif detector == 2:
        fileName = './data/det2_hits.csv'

    detector_hits = pd.read_csv(fileName,
                                 names=["x", "y", "z","energy"],
                                 dtype={"x":np.float64,
                                        "y": np.float64, "z":np.float64},
                                 error_bad_lines=False,
                                 skiprows=1,
                                 engine='c')

    return [detector_hits["x"], detector_hits["z"]]
