#!/usr/bin/python3.5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time

def plotResults(energy):
    d = pd.read_csv('./data/results.txt')


    fig = plt.figure()

    # Mean
    plt.plot(d.index, d['Theta_mean'], color='b')
    plt.fill_between(d.index, d['Theta_mean']-1.96*d['Theta_std'], d['Theta_mean']+1.96*d['Theta_std'],
                     color='blue', alpha=0.2, label='95% confidence')

    # Median
    plt.plot(d.index, d['Theta_median'], color='g')

    # Skew normal fit
    plt.plot(d.index, d['Theta_snormfit'], color='purple', label='Theta Skewnorm Fit')
    plt.fill_between(d.index, d['Theta_snormfit']-1.96*d['T_s_snf'], d['Theta_snormfit']+1.96*d['T_s_snf'],
                     color='orange', alpha=0.5, label='95% skewnorm fit confidence')

    # Actual
    plt.plot(d['Theta_actual'], linestyle='-.', color='r')


    n_particles = d['Number_Particles'][0]
    plt.text(min(d.index), max(d.index)+5, 'E = %i keV, N = %i particles ' % (int(energy), int(n_particles)) , fontsize=10)
    plt.ylabel('Angle (degrees)')
    plt.title('Incident Angle Estimation Methods')
    plt.grid()
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode='expand', borderaxespad=0.)

    fileName = '../results/angle_est_%i_kev_' % int(energy) + str(time.strftime("%m%d_%H%M%S")) + '.png'
    fig.savefig(fileName, dpi=fig.dpi)
