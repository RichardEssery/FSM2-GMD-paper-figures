"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 9. Maximum sub-canopy snow mass, duration of snow cover on the ground and fraction of total snowfall
sublimating in the 16 Alptal forest simulations numbered in Table 1.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
fig = plt.figure(figsize=(7.35,6))

table = np.loadtxt('Figure09.csv',delimiter=',')
conf = table[:,0].astype(int)
mass = table[:,1]
durn = table[:,2]
subl = table[:,3]

plt.scatter(mass,durn,c=subl,vmin=0.1,vmax=0.16)
plt.colorbar(label='Fraction of snowfall sublimating')

plt.annotate('0',(mass[0],durn[0]-3),fontsize=14)
plt.annotate('1',(mass[1]-2,durn[1]-3),fontsize=14)
plt.annotate('2',(mass[2],durn[2]+1),fontsize=14)
plt.annotate('3',(mass[3]-2,durn[3]+1),fontsize=14)
plt.annotate('4',(mass[4],durn[4]-3),fontsize=14)
plt.annotate('5',(mass[5]-2,durn[5]-3),fontsize=14)
plt.annotate('6',(mass[6],durn[6]+1),fontsize=14)
plt.annotate('7',(mass[7],durn[7]-3),fontsize=14)
plt.annotate('8',(mass[8],durn[8]-3),fontsize=14)
plt.annotate('9',(mass[9],durn[9]-3),fontsize=14)
plt.annotate('10',(mass[10]-4,durn[10]-3),fontsize=14)
plt.annotate('11',(mass[11],durn[11]+1),fontsize=14)
plt.annotate('12',(mass[12]-4,durn[12]+1),fontsize=14)
plt.annotate('13',(mass[13]-4,durn[13]+1),fontsize=14)
plt.annotate('14',(mass[14],durn[14]+1),fontsize=14)
plt.annotate('15',(mass[15],durn[15]+1),fontsize=14)

plt.xlim(150,220)
plt.xticks([160,170,180,190,200,210])
plt.xlabel('Maximum snow mass (kg m$^{-2}$)')
plt.ylabel('Snow cover duration (days)')
plt.ylim(70,130)
plt.tight_layout()
plt.savefig('Figure09.pdf')

