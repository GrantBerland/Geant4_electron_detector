
import pandas as pd
import numpy as np
from fnc_fitGauss import fit2DnormalDistribution


initial_params = pd.read_csv('./data/init_pos.csv',
                             names=["x","y","z","momX","momY","momZ"],
                             dtype=np.float64)


mom_mag = np.sqrt(initial_params['momX'][1]**2 +
                  initial_params['momY'][1]**2 +
                  initial_params['momZ'][1]**2)

theta_actual = np.rad2deg(np.arctan2(initial_params['momX'][1], initial_params['momY'][1]))
phi_actual = np.rad2deg(np.arctan2(initial_params['momZ'][1], initial_params['momY'][1]))


det1 = fit2DnormalDistribution(detector=1)
det2 = fit2DnormalDistribution(detector=2)

x1, z1 = det1['Mean']
x2, z2 = det2['Mean']

# In centimeters
dx = x1 - x2
dz = z1 - z2

gap = 0.25 # cm

theta_exp = np.rad2deg(np.arctan2(dz, gap))
phi_exp = np.rad2deg(np.arctan2(dx, gap))

print("Experimental: " + str(theta_exp) + " " +  str(phi_exp))
print("Actual: " + str(theta_actual) + " " +  str(phi_actual))
