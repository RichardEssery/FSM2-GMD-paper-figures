"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure 7. Simulations of (a) average sub-canopy wind speeds and (b) ratios between sub-canopy
and open wind speeds, compared with measurements in 22 forest stands. Simulations with one and
two canopy layers are indistinguishable.
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.figure(figsize=(12,6))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

CANRAD = np.loadtxt('Figure07.dat',usecols=0)
Uobs  = np.loadtxt('Figure07.dat',usecols=1)
Umod  = np.loadtxt('Figure07.dat',usecols=2)
robs   = np.loadtxt('Figure07.dat',usecols=3)
rmod   = np.loadtxt('Figure07.dat',usecols=4)

ax1.plot(Uobs,Umod,'ko')
ax2.plot(robs,rmod,'ko')

ax1.plot([0,2],[0,2],'k',lw=1)
ax1.set_xlim(0,1.5)
ax1.set_xlabel('Measured')
ax1.set_ylim(0,1.5)
ax1.set_yticks([0,0.5,1,1.5])
ax1.set_ylabel('Modelled')
ax1.set_title('(a) Forest wind speed (m s$^{-1}$)')

ax2.plot([0,1],[0,1],'k',lw=1)
ax2.set_xlim(0,1)
ax2.xaxis.set_minor_locator(MultipleLocator(0.1))
ax2.set_xlabel('Measured')
ax2.set_ylim(0,1)
ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
ax2.set_ylabel('Modelled')
ax2.set_title('(b) Forest/open wind speed ratio (-)')

plt.tight_layout()
plt.savefig('Figure07.pdf')
