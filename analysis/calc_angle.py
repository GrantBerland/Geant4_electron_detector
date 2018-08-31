
import pandas as pd
import numpy as np
from fnc_fitGauss import fit2DnormalDistribution


initial_params = pd.read_csv('./data/init_pos.csv',
                             names=["x","y","z","momX","momY","momZ"],
                             dtype=np.float64)


mom_mag = np.sqrt(initial_params['momX'][0]**2 +
                  initial_params['momY'][0]**2 +
                  initial_params['momZ'][0]**2)

theta_actual = np.rad2deg(np.arctan2(initial_params['momX'][0], initial_params['momY'][0]))
phi_actual = np.rad2deg(np.arctan2(initial_params['momZ'][0], initial_params['momY'][0]))


det1 = fit2DnormalDistribution(detector=1)
det2 = fit2DnormalDistribution(detector=2)

x1, z1 = det1['Mean']
x2, z2 = det2['Mean']

print(x1, z1)

# In centimeters
dx = x1 - x2
dz = z1 - z2

gap = 0.25 # cm

theta_exp = np.rad2deg(np.arctan2(dz, gap))
phi_exp = np.rad2deg(np.arctan2(dx, gap))

print("Experimental: theta=" + str(theta_exp) + ", phi=" +  str(phi_exp))
print("Actual: theta=" + str(theta_actual) + ", phi=" +  str(phi_actual))


if(theta_actual == 0 or phi_actual == 0):
  # Rotates frame by 90 degrees if 0 is an actual angle to avoid divide by 0 warning
  theta_error = ((theta_exp+90) - (theta_actual+90))/(theta_actual+90)*100
  phi_error = ((phi_exp+90) - (phi_actual+90))/(phi_actual+90)*100
else:
  theta_error = (theta_exp - theta_actual)/theta_actual*100
  phi_error = (phi_exp - phi_actual)/phi_actual*100




print("Theta error: " + str(theta_error) + " %")
print("Phi error: " + str(phi_error) + " %")
