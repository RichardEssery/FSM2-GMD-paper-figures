"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure A1. Snow mass simulated with the 16 canopy configurations of FSM2 (black lines), simulated by the 33 models
that participated in SnowMIP2 (grey lines) and measured at the four SnowMIP2 forest sites (red points). Snow mass
measurements for the first winter at each site were shared with the SnowMIP2 participants to allow model calibration,
but the models still produced a wide range of results (Rutter et al., 2009).
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.figure(figsize=(12,16))

mons = ['S','O','N','D','J','F','M','A','M','J','J','A','S','O','N','D','J','F','M','A','M','J']
tiks = np.linspace(0,365+270,22)
models =  ['2LM','ACA','CL3','CLA','CLI','COL','COU','CRH','ESC','ISE',
           'ISF','JUL','MAP','MAT','MOS','NOH','RCA','S17','SAS','SB2',
           'SB3','SIB','SNO','SNP','SPO','SRG','SSI','SWA','TES','UEB',
           'UUE','VEG','VIC']
title = ['Alptal 2002-2004','BERMS OJP 2002-2004','Fraser forest 2003-2005','Hyytiala 2003-2005']
sites = ['Alp_for_0203','Alp_for_0304','BRM_for_0203','BRM_for_0304','Frs_for_0304','Frs_for_0405','Hyy_for_0304','Hyy_for_0405']
off = [30,30+365,0,365,61,30+365,30,30+365]
for s in range(4):
    plt.subplot(4,1,s+1)
    for y in range(2):
        site = sites[2*s+y]
        offset = off[2*s+y]
        for model in models:
            try:
                swe = np.loadtxt('FigureA1data/'+model+'_'+site+'.dat')
                swe[swe<=0] = np.NaN
                days = np.arange(len(swe))/48 + offset
                plt.plot(days,swe,'grey')
            except:
                pass
        for CANINT in ['1','2']:
            for CANMOD in ['1','2']:
                for CANRAD in ['1','2']:
                    for CANUNL in ['1','2']:
                        swe = np.loadtxt('FigureA1data/FSM2_'+CANINT+CANMOD+CANRAD+CANUNL+'_'+site+'.dat')
                        days = np.arange(len(swe))/48 + offset
                        plt.plot(days,swe,'k')
        swe = np.loadtxt('FigureA1data/SWEobs_'+site+'.dat')
        swe[swe<=0] = np.NaN
        days = np.arange(len(swe)) + offset
        plt.plot(days,swe,'ro')
    plt.xlim(0,365+270)
    plt.xticks(tiks,mons)
    if s==1:
        plt.ylim(0,150)
    else:
        plt.ylim(0,300)
    plt.ylabel('Snow mass (kg m$^{-2}$)')
    plt.title(title[s],position=(0.5,0.85))
        
plt.tight_layout()
plt.savefig('FigureA1.pdf')


