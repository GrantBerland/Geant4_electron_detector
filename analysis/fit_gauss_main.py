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

Xin = detector1_hits["x"]
Yin = detector1_hits["z"]

X, Y = np.meshgrid(Xin, Yin)

counts,xbins,ybins,image = plt.hist2d(Xin,Yin,bins=200)
plt.colorbar()
plt.contour(counts.transpose())#,extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=1)
plt.xlim([-5,5]); plt.xlabel("x [cm]")
plt.ylim([-5,5]); plt.ylabel("z [cm]")


'''
data = fit.gaussian(3, 100, 100, 20, 40)(xbins, ybins)


#plt.matshow(data, cmap=plt.cm.gist_earth_r)

params = fit.fitgaussian(data)
fit = fit.gaussian(*params)

plt.contour(fit(*np.indices(data.shape)), cmap=plt.cm.copper)

ax = plt.gca()
(height, x, y, width_x, width_y) = params
'''

plt.show()

