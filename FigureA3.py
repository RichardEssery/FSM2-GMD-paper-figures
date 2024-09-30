"""
A Flexible Snow Model (FSM 2.1.0) including a forest canopy
Figure A3. Differences between simulations of Northern Hemisphere snow cover by the nine 
models that participated in LS3MIP (van den Hurk et al. 2016) and IMS on 1 March 2010.
"""
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

fig = plt.figure(figsize=(16,6.7))
plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

ims = Dataset('FigureA3.nc') 
dsnc = ims.variables['dsnc'][:,:,:]

for n in range(9):
    plt.subplot(4,3,n+1)
    im = plt.imshow(dsnc[n,:,:],cmap='coolwarm_r',origin='lower',vmin=-1,vmax=1)
    plt.xticks([])
    plt.yticks([])
    if n == 8:
        cax = fig.add_axes([0.349,0.2,0.305,0.03])
        fig.colorbar(im,cax=cax,label='model - IMS snow cover difference',orientation='horizontal',ticks=[-1,0,1])

plt.tight_layout()
plt.savefig('FigureA3.pdf')
