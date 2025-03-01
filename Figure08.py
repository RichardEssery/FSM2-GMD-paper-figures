"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 8. Simulations (lines) and observations (points) for the Alptal forest and meadow sites in 2004-2005.
Albedo, transmission and longwave radiation fluxes are daily values. Subjective canopy snow load observations
are scaled to the model's canopy capacity (dashed line in b).
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.figure(figsize=(16,12))

ax11 = plt.subplot(321)
ax12 = plt.subplot(322)
ax21 = plt.subplot(323)
ax22 = plt.subplot(324)
ax31 = plt.subplot(325)
ax32 = plt.subplot(326)
ax12a = ax12.twinx()

nh = 5832
days = 24*np.arange(nh/24)
firsts = [0,743,1463,2207,2951,3623,4367,5087,5832]
months = ['O','N','D','J','F','M','A','M','J']

swe = np.loadtxt('Figure08swemod.dat')
svg = np.loadtxt('Figure08svgmod.dat')
alb = np.loadtxt('Figure08albmod.dat')
trn = np.loadtxt('Figure08SWtrmod.dat')
LWup = np.loadtxt('Figure08LWupmod.dat')
LWsub = np.loadtxt('Figure08LWsubmod.dat')
for n in range(16):
    ax11.plot(swe[:,n],'k')
    ax12.plot(svg[:,n],'k')
    ax21.plot(days,alb[:,n],'k')
    ax22.plot(days,LWup[:,n],'k')
    ax31.plot(days,trn[:,n],'k')
    ax32.plot(days,LWsub[:,n],'k')
                
ax11.plot(swe[:,16],'b')
ax21.plot(days,alb[:,16],'b')
ax22.plot(days,LWup[:,16],'b')
            
alb = np.loadtxt('Figure08meadowobs.dat',usecols=0)
Lup = np.loadtxt('Figure08meadowobs.dat',usecols=1)
snd = np.loadtxt('Figure08meadowobs.dat',usecols=2)
swe = np.loadtxt('Figure08meadowobs.dat',usecols=3)
ax11.plot(days,swe,'bo',ms=4)
ax21.plot(days,alb,'bo',ms=3)
ax22.plot(days,Lup,'bo',ms=3)

Scap = 4.4*3.96
alb = np.loadtxt('Figure08forestobs.dat',usecols=0)
Lup = np.loadtxt('Figure08forestobs.dat',usecols=1)
Ldn = np.loadtxt('Figure08forestobs.dat',usecols=2)
svg = (Scap/8)*np.loadtxt('Figure08forestobs.dat',usecols=3)
swe = np.loadtxt('Figure08forestobs.dat',usecols=4)
trn = np.loadtxt('Figure08forestobs.dat',usecols=5)
ax11.plot(days,swe,'ro',ms=4)
ax12.plot(days,svg,'ro',ms=4)
ax12.plot([0,nh],[Scap,Scap],'k--')
ax12.text(20,15.4,'canopy capacity')
ax21.plot(days,alb,'ro',ms=3)
ax22.plot(days,Lup,'ro',ms=3)  
ax31.plot(days,trn,'ro',ms=3)
ax32.plot(days,Ldn,'ro',ms=3)  
            
ax11.set_xlim(0,nh)
ax12.set_xlim(0,nh)
ax21.set_xlim(0,nh)
ax22.set_xlim(0,nh)
ax31.set_xlim(0,nh)
ax32.set_xlim(0,nh)
ax11.set_xticks(firsts)
ax11.set_xticklabels(months)
ax12.set_xticks(firsts)
ax12.set_xticklabels(months)
ax21.set_xticks(firsts)
ax21.set_xticklabels(months)
ax22.set_xticks(firsts)
ax22.set_xticklabels(months)
ax31.set_xticks(firsts)
ax31.set_xticklabels(months)
ax32.set_xticks(firsts)
ax32.set_xticklabels(months)
ax11.set_ylim(0,400)
ax12.set_ylim(0,20)
ax21.set_ylim(0,1)
ax22.set_ylim(200,400)
ax31.set_ylim(0,0.2)
ax32.set_ylim(200,400)
ax12.set_yticks([0,10,20])
ax22.set_yticks([200,300,400])
ax31.set_yticks([0,0.1,0.2])
ax32.set_yticks([200,300,400])
ax21.yaxis.set_minor_locator(MultipleLocator(0.1))
ax11.set_title('(a) Open and sub-canopy snow mass (kg m$^{-2}$)')
ax12.set_title('(b) Canopy snow mass (kg m$^{-2}$)')
ax21.set_title('(c) Open and above-canopy albedo (-)')
ax22.set_title('(d) Open and above-canopy outgoing LW (W m$^{-2}$)')
ax31.set_title('(e) Sub-canopy SW transmission (-)')
ax32.set_title('(f) Sub-canopy incoming LW (W m$^{-2}$)')

ax11.plot(0,0,'b',label='meadow model')
ax11.plot(0,0,'bo',ms=4,label='meadow obs')
ax11.plot(0,0,'k',label='forest model')
ax11.plot(0,0,'ro',ms=4,label='forest obs')
ax11.legend(labelspacing=0.3,loc='upper left')

ax12a.set_ylim(0,20)
ax12a.set_yticks((Scap/8)*np.arange(9))
ax12a.set_yticklabels(['0','1','2','3','4','5','6','6','8'])
ax12a.set_ylabel('canopy snow load')

plt.tight_layout()
plt.savefig('Figure08.pdf')




