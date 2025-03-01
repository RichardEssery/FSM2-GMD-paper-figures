"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 11. Northern Hemisphere deciduous and evergreen forest fractions from Lawrence and Chase (2007).
"""
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from netCDF4 import Dataset
import numpy as np

plt.figure(figsize=(12,3))
plt.rcParams['font.size'] = 16
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

gg = np.ones((256,4))
gg[:,0] = np.linspace(0.75,0,256)
gg[:,1] = np.linspace(0.75,1,256)
gg[:,2] = np.linspace(0.75,0,256)
greygreen = ListedColormap(gg)
gb = np.ones((256,4))
gb[:,0] = np.linspace(0.75,0,256)
gb[:,1] = np.linspace(0.75,0,256)
gb[:,2] = np.linspace(0.75,1,256)
greyblue = ListedColormap(gb)

fveg = Dataset('Figure11.nc','r')
dec = fveg.variables['dec'][:,:]
evg = fveg.variables['evg'][:,:]

plt.imshow(evg,cmap=greyblue,origin='lower',vmin=0,vmax=1)
plt.colorbar(label='evergreen fraction',pad=-0.05,shrink=0.76,ticks=[0,1])
plt.imshow(dec,alpha=0.5,cmap=greygreen,origin='lower',vmin=0,vmax=1)
plt.colorbar(label='deciduous fraction',pad=0.03,shrink=0.76,ticks=[0,1])
plt.xticks([])
plt.yticks([])

plt.savefig('Figure11.pdf')

