#!/usr/bin/python3.5

from astroML.stats import fit_bivariate_normal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

detector1_hits = pd.read_csv("./data/hits_det1.csv",
                             names=["x", "y", "z", "mom_x", "mom_y", "mom_z"],
                             dtype=np.float64)

detector2_hits = pd.read_csv("./data/hits_det2.csv",
                             names=["x", "y", "z", "mom_x", "mom_y", "mom_z"],
                             dtype=np.float64)

# Hit data from detector 1
X1 = detector1_hits["x"]
Y1 = detector1_hits["z"]

# Hit data from detector 2
X2 = detector2_hits["x"]
Y2 = detector2_hits["z"]

(mu_nr, sigma1_nr,
     sigma2_nr, alpha_nr) = fit_bivariate_normal(X1, Y1, robust=True)

fig = plt.figure()
ax = fig.add_subplot(1,2,1)

# Scatter plot of hit data
ax.scatter(X1, Y1, s=2, lw=0, c='k', alpha=0.5)
sigma_conf = 3

E = Ellipse(mu_nr, sigma1_nr * sigma_conf, sigma2_nr * sigma_conf,
            (alpha_nr * 180. / np.pi), ec='k', fc='none', linestyle='dotted')

ax.add_patch(E)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel("x [cm]")
ax.set_ylabel("z [cm]")
ax.text(0.04, 0.96, "Detector 1",
            ha='left', va='top', transform=ax.transAxes)

plt.show()
