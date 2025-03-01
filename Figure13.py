"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 13. Northern Hemisphere snow cover fraction and albedo maps for 1 March 2010 from FSM2, IMS and MODIS MCD43C3.
The FSM2 simulation has two canopy layers, two-stream radiative transfer, nonlinear canopy snow interception and
temperature/wind-dependent unloading.
"""
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

plt.figure(figsize=(16,6))
plt.rcParams['font.size'] = 16
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

fig13 = Dataset('Figure13.nc','r')
fig13a = fig13.variables['fig12a']
fig13b = fig13.variables['fig12b']
fig13c = fig13.variables['fig12c']
fig13d = fig13.variables['fig12d']
fig13e = fig13.variables['fig12e']
fig13f = fig13.variables['fig12f']

plt.subplot(321)   
plt.imshow(fig13a,origin='lower',vmin=0,vmax=1)
plt.colorbar()
plt.title('(a) FSM2 snow cover fraction')
plt.xticks([])
plt.yticks([])

plt.subplot(322)   
plt.imshow(fig13b,origin='lower',vmin=0,vmax=1)
plt.colorbar()
plt.title('(b) FSM2 albedo')
plt.xticks([])
plt.yticks([])

plt.subplot(323)
plt.imshow(fig13c,origin='lower',vmin=0,vmax=1)
plt.colorbar()
plt.title('(c) IMS snow cover fraction')
plt.xticks([])
plt.yticks([])

plt.subplot(324)
plt.imshow(fig13d,origin='lower',vmin=0,vmax=1)
plt.colorbar()
plt.title('(d) MCD43C3 albedo')
plt.xticks([])
plt.yticks([])

plt.subplot(325)
plt.imshow(fig13e,cmap='coolwarm_r',origin='lower',vmin=-1,vmax=1)
plt.colorbar()
plt.title('(e) FSM2 - IMS snow cover difference')
plt.xticks([])
plt.yticks([])

plt.subplot(326)
plt.imshow(fig13f,cmap='coolwarm_r',origin='lower',vmin=-0.5,vmax=0.5)
plt.colorbar(ticks=[-0.5,0,0.5])
plt.title('(f) FSM2 - MCD43C3 albedo difference')
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.savefig('Figure13.pdf')
