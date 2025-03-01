"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 6. Simulations with one canopy layer (open circles) and two canopy layers (closed circles)
of (a) average sub-canopy downwards longwave radiation and (b) canopy longwave enhancement, 
compared with measurements in 10 forest stands.
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
ax1.plot([200,300],[200,300],'k',lw=1)
ax2.plot([1,2],[1,2],'k',lw=1)

CANMOD = np.loadtxt('Figure06.dat',usecols=0)
tobs   = np.loadtxt('Figure06.dat',usecols=1)
tmod   = np.loadtxt('Figure06.dat',usecols=2)
eobs   = np.loadtxt('Figure06.dat',usecols=3)
emod   = np.loadtxt('Figure06.dat',usecols=4)

ax1.plot(tobs[CANMOD==1],tmod[CANMOD==1],'ko',mfc='w')
ax1.plot(tobs[CANMOD==2],tmod[CANMOD==2],'ko')
ax2.plot(eobs[CANMOD==1],emod[CANMOD==1],'ko',mfc='w')
ax2.plot(eobs[CANMOD==2],emod[CANMOD==2],'ko')

ax1.set_xlim(200,300)
ax1.set_ylim(200,300)
ax1.set_xticks([200,250,300])
ax1.set_yticks([200,250,300])
ax1.set_xlabel('Measured')
ax1.set_ylabel('Modelled')
ax1.set_title('(a) Sub-canopy LW (W m$^{-2}$)')

ax2.set_xlim(1,1.2)
ax2.set_ylim(1,1.2)
ax2.set_xticks([1,1.1,1.2])
ax2.set_yticks([1,1.1,1.2])
ax2.set_xlabel('Measured')
ax2.set_ylabel('Modelled')
ax2.set_title('(b) Canopy LW enhancement (-)')

plt.tight_layout()
plt.savefig('Figure06.pdf')
