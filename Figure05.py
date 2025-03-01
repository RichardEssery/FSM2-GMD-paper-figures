"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 5. Beer's Law (open circles) and two-stream approximation (closed circles) simulations
of (a) average sub-canopy downwards shortwave radiation and (b) canopy shortwave transmission,
compared with measurements in 10 forest stands.
Simulations with one and two canopy layers are indistinguishable.
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

CANRAD = np.loadtxt('Figure05.dat',usecols=0)
SWobs  = np.loadtxt('Figure05.dat',usecols=1)
SWmod  = np.loadtxt('Figure05.dat',usecols=2)
tobs   = np.loadtxt('Figure05.dat',usecols=3)
tmod   = np.loadtxt('Figure05.dat',usecols=4)

ax1.plot(SWobs[CANRAD==1],SWmod[CANRAD==1],'ko',mfc='w')
ax1.plot(SWobs[CANRAD==2],SWmod[CANRAD==2],'ko')
ax2.plot(tobs[CANRAD==1],tmod[CANRAD==1],'ko',mfc='w')
ax2.plot(tobs[CANRAD==2],tmod[CANRAD==2],'ko')

ax1.plot([0,200],[0,200],'k',lw=1)
ax1.set_xlim(0,200)
ax1.set_xticks([0,100,200])
ax1.set_xlabel('Measured')
ax1.set_ylim(0,200)
ax1.set_yticks([0,100,200])
ax1.set_ylabel('Modelled')
ax1.set_title('(a) Sub-canopy SW (W m$^{-2}$)')

ax2.plot([0,1],[0,1],'k',lw=1)
ax2.set_xlim(0,1)
ax2.xaxis.set_minor_locator(MultipleLocator(0.1))
ax2.set_xlabel('Measured')
ax2.set_ylim(0,1)
ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
ax2.set_ylabel('Modelled')
ax2.set_title('(b) Canopy SW transmission (-)')

plt.tight_layout()
plt.savefig('Figure05.pdf')
