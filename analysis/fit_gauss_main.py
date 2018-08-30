import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import fit2dGaussian as fit
from astroML.stats import fit_bivariate_normal
import sys

# plotOn = 1 for plotting
plotOn = sys.argv[1]

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

if plotOn == '1':

    fig = plt.figure()
    fig.subplots_adjust(left=0.1, right=0.95, wspace=0.05,
                    bottom=0.15, top=0.95)
    ax = fig.add_subplot(1,2,1)

    # Creates histogram from hit data, look into auto bin number
    counts,xbins,ybins,image = plt.hist2d(X1,Y1, bins=300, normed=True)
    plt.contour(counts.transpose(),extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=1)
    plt.xlim([-5,5]); plt.xlabel("x [cm]")
    plt.ylim([-5,5]); plt.ylabel("z [cm]")
    plt.title("Detector 1")

    ax = fig.add_subplot(1,2,2)
    counts,xbins,ybins,image = plt.hist2d(X2,Y2, bins=150, normed=True)
    plt.contour(counts.transpose(),extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=1)
    plt.xlim([-5,5]); plt.xlabel("x [cm]")
    plt.ylim([-5,5]); plt.ylabel("z [cm]")
    plt.title("Detector 2")

(mu_nr, sigma1_nr,
     sigma2_nr, alpha_nr) = fit_bivariate_normal(X1, Y1, robust=False)

'''
data = fit.twoD_Gaussian((X1, Y1), 3, 100, 100, 20, 40, 0, 10)

# plot twoD_Gaussian data generated above
plt.figure()
plt.plot(data.reshape(int(np.sqrt(data.size)), int(np.sqrt(data.size))))
plt.colorbar()
'''

plt.show()
