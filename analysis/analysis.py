
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D, axes3d




initialPositionData = pd.read_csv("./data/init_pos.csv",
                                  names=["x", "y", "z"],
                                  dtype=np.float64)

detector1_hits = pd.read_csv("./data/hits_det1.csv",
                             names=["x", "y", "z", "mom_x", "mom_y", "mom_z"],
                             dtype=np.float64)

detector2_hits = pd.read_csv("./data/hits_det2.csv",
                             names=["x", "y", "z", "mom_x", "mom_y", "mom_z"],
                             dtype=np.float64)


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

x = detector1_hits["x"]
y = detector1_hits["z"]
hist, xedges, yedges = np.histogram2d(x, y, bins=15, range=[[-5, 5], [-5, 5]])


xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the 16 bars.
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.xlabel("x [cm]")
plt.ylabel("z [cm]")
plt.title("Detector 1")


fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

x2 = detector2_hits["x"]
y2 = detector2_hits["z"]
hist2, xedges2, yedges2 = np.histogram2d(x2, y2, bins=20, range=[[-5, 5], [-5, 5]])


xpos2, ypos2 = np.meshgrid(xedges2[:-1] + 0.25, yedges2[:-1] + 0.25)
xpos2 = xpos2.flatten('F')
ypos2 = ypos2.flatten('F')
zpos2 = np.zeros_like(xpos2)

# Construct arrays with the dimensions for the 16 bars.
dx2 = 0.5 * np.ones_like(zpos2)
dy2 = dx2.copy()
dz2 = hist2.flatten()

ax2.bar3d(xpos2, ypos2, zpos2, dx2, dy2, dz2, color='b', zsort='average')
plt.xlabel("x [cm]")
plt.ylabel("z [cm]")
plt.title("Detector 2")


plt.show()

