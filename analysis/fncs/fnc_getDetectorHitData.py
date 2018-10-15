#!/usr/bin/python3.5


import pandas as pd
import numpy as np


def getDetectorHitData(detector):
    detector_hits = pd.read_csv('./data/hits.csv',
                                 names=["det","x", "y", "z","energy"],
                                 dtype={"det": np.int32, "x":np.float64,
                                        "y": np.float64, "z":np.float64, "energy":np.float64},
                                 error_bad_lines=False,
                                 engine='c')

    return detector_hits["x"], detector_hits["z"]
