#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:16:12 2020

@author: lshuns

Plot the diffraction integral for SIS lens
 using results calculated by MATHEMATICA 
"""

import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt



# data directory
indir = './Mathematica/data/Frel/SIS/'
# dimensionless frequency 
w = np.loadtxt(indir + 'w.txt')
# impact parameter y = 1
# abs for amplitude, arg for phase
Frel10_abs = np.loadtxt(indir + 'Frel10_abs.txt')
Frel10_arg = np.loadtxt(indir + 'Frel10_arg.txt')
# impact parameter y = 2
# abs for amplitude, arg for phase
Frel20_abs = np.loadtxt(indir + 'Frel20_abs.txt')
Frel20_arg = np.loadtxt(indir + 'Frel20_arg.txt')
# impact parameter y = 3
# abs for amplitude, arg for phase
Frel30_abs = np.loadtxt(indir + 'Frel30_abs.txt')
Frel30_arg = np.loadtxt(indir + 'Frel30_arg.txt')
# impact parameter y = 4
# abs for amplitude, arg for phase
Frel40_abs = np.loadtxt(indir + 'Frel40_abs.txt')
Frel40_arg = np.loadtxt(indir + 'Frel40_arg.txt')


# general setting for plot
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True

fig = plt.figure()

# angle (phase)
ax = plt.axes([0.12, 0.5, 0.81, 0.4])
plt.plot(w, Frel10_arg, color='r', label='$y=1$')
plt.plot(w, Frel20_arg, color='b', label='$y=2$')
# plt.plot(w, Frel30_arg, color='p', label='$y=3$')
plt.plot(w, Frel40_arg, color='m', label='$y=4$')

plt.xlim([0.05, 10])
# plt.ylim([-0.05, 0.1])
plt.legend(frameon=False, loc='best', fontsize=12)
plt.xscale('log')
plt.ylabel(r'${\rm arg}[F_{\rm rel}(w)]$', fontsize=16)
plt.title(r'SIS', fontsize=14)

# amplitude
ax1 = plt.axes([0.12, 0.1, 0.81, 0.4])
plt.plot(w, Frel10_abs, color='r')
plt.plot(w, Frel20_abs, color='b')
# plt.plot(w, Frel30_abs, color='p')
plt.plot(w, Frel40_abs, color='m')

plt.xlim([0.05, 10])
# plt.ylim([-0.8,0.8])
plt.xlabel(r'$w$', fontsize=16)
plt.ylabel(r'$|F_{\rm rel}(w)|$', fontsize=16)
plt.xscale('log')
plt.show()
# plt.savefig('./Mathematica/plot/SIS_ang_amp.png')
