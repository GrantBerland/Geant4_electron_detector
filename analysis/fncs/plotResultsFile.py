#!/usr/bin/python3.5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time

def plotResults(energy):
    d = pd.read_csv('./data/results.txt')


    fig = plt.figure()

    # Mean
    plt.plot(d.index, d['Theta_est'], color='b', label='Theta Estimate')
    plt.fill_between(d.index, d['Theta_est']-d['Theta_std'], d['Theta_est']+d['Theta_std'],
                     color='blue', alpha=0.2, label=None)

    # Median
    #plt.plot(d.index, d['Theta_median'], color='g')

    # Skew normal fit
    #plt.plot(d.index, d['Theta_snormfit'], color='purple', label=None)
    plt.fill_between(d.index, d['Theta_est']-d['Theta_std'], d['Theta_est']+d['Theta_std'],
                     color='orange', alpha=0.5, label=r'1 $\sigma$ confidence')
    plt.fill_between(d.index, d['Theta_est']-2*d['Theta_std'], d['Theta_est']+2*d['Theta_std'],
                     color='orange', alpha=0.25, label=r'2 $\sigma$ confidence')
    # Actual
    plt.plot(d['Theta_actual'], linestyle='-.', color='r', label='Theta Actual')


    n_particles = d['Number_Particles'][0]
    plt.text(min(d.index), max(d.index)+5, 'E = %i keV, N = %i particles ' % (int(energy), int(n_particles)) , fontsize=10)
    plt.ylabel('Angle (degrees)')
    plt.grid()
    plt.legend()

    fileName = '../results/angle_est_%i_kev_' % int(energy) + str(time.strftime("%m%d_%H%M%S")) + '.png'
    fig.savefig(fileName, dpi=fig.dpi)
