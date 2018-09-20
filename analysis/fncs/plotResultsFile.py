#!/usr/bin/python3.5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotResults(energy):
    d = pd.read_csv('./data/results.txt')


    fig = plt.figure()

    # Mean
    plt.plot(d.index, d['Theta_mean'], color='b', label='Theta Mean')
    plt.fill_between(d.index, d['Theta_mean']-1.96*d['Theta_std'], d['Theta_mean']+1.96*d['Theta_std'],
                     color='blue', alpha=0.2, label='95% confidence')


    # Median
    plt.plot(d.index, d['Theta_median'], color='g', label='Theta median')

    # Normal fit
    #plt.errorbar(x=d.index, y=d['Theta_normfit'], yerr=(d['T_s_nf']/np.sqrt(d['Number_Particles'])))

    # Actual
    plt.plot(d['Theta_actual'], linestyle='-.', color='r')


    n_particles = d['Number_Particles'][0]
    plt.text(min(d.index), max(d.index)+5, 'E = %i keV, N = %i particles ' % (int(energy), int(n_particles)) , fontsize=10)
    plt.ylabel('Angle (degrees)')
    plt.title('Incident Angle Estimation Methods')
    plt.grid()
    plt.legend()

    fig.savefig('../results/angle_est_%i_kev.png' % int(energy), dpi=fig.dpi)
