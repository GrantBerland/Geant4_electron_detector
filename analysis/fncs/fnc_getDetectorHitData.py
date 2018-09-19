#!/usr/bin/python3.5


import pandas as pd
import numpy as np


def getDetectorHitData(detector):
    detector_hits = pd.read_csv('./data/hits.csv',
                                 names=["det","x", "y", "z","energy", "code"],
                                 dtype={"det": np.int32, "x":np.float64,
                                        "y": np.float64, "z":np.float64,
                                         "code": np.unicode_},
                                 error_bad_lines=False,
                                 skiprows=1,
                                 engine='c')



    # Hit data from detector
    whichDetectorIndex = detector_hits.index[(detector_hits["det"] == detector)
                                             & (detector_hits["code"] == "GH")].tolist()


    return [detector_hits["x"][whichDetectorIndex], detector_hits["z"][whichDetectorIndex]]
