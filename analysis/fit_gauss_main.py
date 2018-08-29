import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import fit2dGaussian as fit


detector1_hits = pd.read_csv("./data/hits_det1.csv",
                             names=["x", "y", "z", "mom_x", "mom_y", "mom_z"],
                             dtype=np.float64)

detector2_hits = pd.read_csv("./data/hits_det2.csv",
                             names=["x", "y", "z", "mom_x", "mom_y", "mom_z"],
                             dtype=np.float64)

X1 = detector1_hits["x"]
Y1 = detector1_hits["z"]

plt.figure()
counts,xbins,ybins,image = plt.hist2d(X1,Y1,bins=300, normed=True)
#plt.colorbar() # learn how histograms work?
plt.contour(counts.transpose(),extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=1)
plt.xlim([-5,5]); plt.xlabel("x [cm]")
plt.ylim([-5,5]); plt.ylabel("z [cm]")
plt.title("Detector 1")

# Hit data from detector 2
X2 = detector2_hits["x"]
Y2 = detector2_hits["z"]


plt.figure()    # New figure
counts,xbins,ybins,image = plt.hist2d(X2,Y2,bins=100, normed=True)   # Creates histogram from hit data
#plt.colorbar()
plt.contour(counts.transpose(),extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=1)
plt.xlim([-5,5]); plt.xlabel("x [cm]")
plt.ylim([-5,5]); plt.ylabel("z [cm]")
plt.title("Detector 2")

plt.figure()    # New figure

'''
#create data
data = fit.twoD_Gaussian((X1, Y1), 3, 100, 100, 20, 40, 0, 10)

# plot twoD_Gaussian data generated above
plt.figure()
plt.plot(data.reshape(int(np.sqrt(data.size)), int(np.sqrt(data.size))))
plt.colorbar()
'''

plt.show()
