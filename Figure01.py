"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure 1. Heat capacity of snow-free canopies as functions of vegetation area index in MEB, MOSES, VISA and FSM2.
Dots show heat capacities calculated using the method of Gouttevin et al. (2015) with leaf and stem area indices 
for study sites collated by Todt et al. (2018).
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.figure(figsize=(6,6))

LAI = np.arange(0.1,6.1,0.1)

MEB = 0.2*4218*LAI
plt.plot(LAI,MEB,'k:',label='MEB')
MEB = 0.2*4218*LAI + 216*4.4*LAI
#plt.plot(LAI,MEB,label='MEB + snow')

MOSES = 0.57e6*0.1*LAI + 0.11e6*0.65*LAI**1.67
plt.plot(LAI,MOSES,'k-.',label='MOSES')

VISA = 0.02*4.188e6*LAI
plt.plot(LAI,VISA,'k--',label='VISA')

FSM2 = 3.6e4*LAI
plt.plot(LAI,FSM2,'k',label='FSM2')

plt.xlabel('Vegetation area index')
plt.xlim(0,6)
plt.xticks(range(7))
plt.ylabel('Canopy heat capacity (J K$^{-1}$ m$^{-2}$)')
plt.ylim(1e2,1e6)
plt.yscale('log')

LAI = np.array([0,3.24,0.05,1.93,0,3.9,0.89,0])
PAI = [0.44,4.1,1.15,2.41,0.67,5.1,1.14,1.71]
B = np.array([0.0006,0.004,0.0011,0.0036,0.0048,0.0166,0.002,0.004])
zcan = np.array([3.5,25,22,22,5,25,18,18])
Todt = 0.001*900*2800*LAI + 0.5*B*zcan*900*2800
plt.plot(PAI,Todt,'ko',ms=3,label='Todt')

plt.legend(fontsize=18,labelspacing=0.1)
plt.tight_layout()
plt.savefig('Figure01.pdf')


