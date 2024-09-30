"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure 11. Northern Hemisphere seasonal snow area (a) and mass (b) averaged over 2000-2010 from 
16 FSM2 simulations (black lines), nine LS3MIP models (blue lines) and estimates from multi-dataset
historical time series (circles).
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.figure(figsize=(8,8))

ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
mons = np.array([0,31,61,92,122,153,184,212,243,273,304,334])
monames = ['A','S','O','N','D','J','F','M','A','M','J','J']

sce = np.loadtxt('Figure11scemod.dat')
swe = np.loadtxt('Figure11swemod.dat')
models = ['CESM2','CMCC-ESM2','CNRM-CM6','CNRM-ESM2','EC-Earth3','HadGEM3','IPSL-CM6A','MIROC6','MPI-ESM1','UKESM1']
for n in range(10):
    ax1.plot(0.1*sce[:,n],'lightblue')
    ax2.plot(swe[:,n],'lightblue')
for n in range(10,18):
    ax1.plot(0.1*sce[:,n],'k')
    ax2.plot(swe[:,n],'k') 

sce = np.loadtxt('Figure11sceobs.dat')
swe = np.loadtxt('Figure11sweobs.dat')
ax1.plot(mons+15,0.1*sce,'ko')
ax2.plot(mons+15,swe,'ko')

ax1.set_xticks(mons)
ax1.set_xticklabels(monames)
ax1.set_xlim(0,364)
ax1.set_ylabel(r'Snow area ($\times 10^{7}$ km$^2$)')
ax1.set_ylim(0,6)
ax1.yaxis.set_minor_locator(MultipleLocator(1))
ax1.set_title('(a)')

ax2.set_xticks(mons)
ax2.set_xticklabels(monames)
ax2.set_xlim(0,364)
ax2.set_ylabel(r'Snow mass ($\times 10^{9}$ kg)')
ax2.set_ylim(0,8)
ax2.yaxis.set_minor_locator(MultipleLocator(1))
ax2.set_title('(b)')

plt.tight_layout()
plt.savefig('Figure11.pdf')
