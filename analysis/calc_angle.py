
import pandas as pd
import numpy as np
from fnc_fitGauss import fit2DnormalDistribution


initial_params = pd.read_csv('./data/init_pos.csv',
                             names=["x","y","z","momX","momY","momZ"],
                             dtype=np.float64)


mom_mag = np.sqrt(initial_params['momX'][1]**2 +
                  initial_params['momY'][1]**2 +
                  initial_params['momZ'][1]**2)

ang1 = np.arccos(initial_params['momX'][1] / mom_mag)
ang2 = np.arccos(initial_params['momY'][1] / mom_mag)
ang3 = np.arccos(initial_params['momZ'][1] / mom_mag)


det1 = fit2DnormalDistribution(detector=1)
det2 = fit2DnormalDistribution(detector=2)

x1, z1 = det1['Mean']
x2, z2 = det2['Mean']

# In centimeters
dx = x1 - x2
dz = z1 - z2

gap = 0.25 # cm

theta = np.rad2deg(np.arctan2(dz, gap))
phi = np.rad2deg(np.arctan2(dx, gap))

print(theta, phi)
print(ang1, ang2, ang3)
