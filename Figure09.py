"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure 9. Sensitivity to canopy density in simulations with the Alptal 2004-2005 meteorology.
(a) Fractions of total snowfall sublimating in simulations with the 16 canopy model configurations.
(b) Contributions of net shortwave radiation, net longwave radiation and sensible heat fluxes to 
energy for melting snow on the ground in simulations with linear interception, one canopy layer,
Beer's Law radiative transfer and time/melt-dependent unloading.
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.figure(figsize=(12,6))

ax1 = plt.subplot(121)
data = np.loadtxt('Figure09a.dat')
VAI = data[:,0]
subl = data[:,1:]         
for n in range(16):
    ax1.plot(VAI,subl[:,n],'k')
ax1.set_xlim(0,6)
ax1.set_xticks(range(7))
ax1.set_ylim(0,0.2)
ax1.set_yticks([0,0.1,0.2])
ax1.set_xlabel('Vegetation area index')
ax1.set_ylabel('Fraction of snowfall sublimating')
ax1.set_title('(a)')
                
ax2 = plt.subplot(122)
data = np.loadtxt('Figure09b.dat')
VAI = data[:,0]
Sfrac = data[:,1]
Lfrac = data[:,2]
Hfrac = data[:,3] 
Efrac = data[:,4] 
Gfrac = data[:,5] 
ax2.plot(VAI,Sfrac,'k',label='$SW_s$')
ax2.plot(VAI,Lfrac,'k--',label='$LW_s$')
ax2.plot(VAI,Hfrac,'k:',label='$H_s$')
ax2.plot([0,6],[0,0],'k',lw=1)
ax2.set_xlabel('Vegetation area index')
ax2.set_xlim(0,6)
ax2.set_xticks(range(7))
ax2.set_ylim(-0.1,1.1)
ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
ax2.set_ylabel('Fraction of melt energy')
ax2.legend(labelspacing=0.3)
ax2.set_title('(b)')

plt.tight_layout()
plt.savefig('Figure09.pdf')


