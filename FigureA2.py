"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure A2. Snow mass simulated with the 16 canopy configurations of FSM2 (black lines), simulated by the 23 models that
participated in ESM-SnowMIP (grey lines) and measured at the three ESM-SnowMIP forest sites (red points) (Menard et al. (2019).
No data were provided for model calibration. The large underestimates in simulated snow mass at the aspen site in 2007-2008
resulted from erroneous input snowfall data.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.figure(figsize=(12,12))

mipdir = '/exports/csce/datastore/geos/groups/boreal/ReSCUES/ESM-SnowMIP/'
models = ['CABLE-SLI','CLASS','CLM5','CoLM','Crocus','ecearth','ESCIMO','htessel','htesselML',
          'ISBA','ISBA-MEB','jsbach3_PF','JSBACH','JULES','MATSIRO','MOSES','ORCHIDEE-TRUNK-E',
          'ORCHIDEE-TRUNK-I','SNOWPACK','SPO','SWAP','VEG3D']  # 'RUC'
title = ['BERMS Old Aspen','BERMS Old Black Spruce','BERMS Old Jack Pine']
sites = ['oas','obs','ojp']
tiks = [92,457,822,1188,1553,1918,2283,2649,3014,3379,3744,4110,4475]

for s, site in enumerate(sites):
    plt.subplot(3,1,s+1)
    for model in models:
        swe = np.loadtxt('FigureA2data/'+model+'_'+site+'.dat')
        days = np.arange(len(swe))/24
        plt.plot(days,swe,'grey')
    for CANINT in ['1','2']:
        for CANMOD in ['1','2']:
            for CANRAD in ['1','2']:
                for CANUNL in ['1','2']:
                    swe = np.loadtxt('FigureA2data/FSM2_'+CANINT+CANMOD+CANRAD+CANUNL+'_'+site+'.dat')
                    days = np.arange(len(swe))/24
                    plt.plot(days,swe,'k')
    swe = np.loadtxt('FigureA2data/SWEobs_'+site+'.dat')
    swe[swe<0] = np.NaN  
    plt.plot(swe,'ro',ms=4)
    plt.xlim(0,13*365)
    plt.xticks(tiks,['1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
    plt.ylim(0,200)
    plt.ylabel('Snow mass (kg m$^{-2}$)')
    plt.title(title[s],position=(0.5,0.85))

plt.tight_layout()
plt.savefig('FigureA2.pdf')
