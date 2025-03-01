"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 4. Wind speeds above, within and below canopies with vegetation area indices
(from right to left) 0, 0.5, 1, 2, 4 and 8.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
fig = plt.figure(figsize=(6,6))

z = np.arange(0.001,2,0.001)
Ud = np.zeros_like(z)
Uo = np.zeros_like(z)
hb = 0.2
z0g = 0.001
z0v = 0.1

plt.fill_between([0,2],[hb,hb],[1,1],color='lightgrey')
for LAI in (0,0.5,1,2,4,8):
    fv = 1 - np.exp(-0.5*LAI)
    d = 0.67
    z0 = z0v
    Ud[z>1] = np.log((z[z>1]-d)/z0) / np.log((1-d)/z0)
    Ud[z<=1] = np.exp(2.5*(z[z<=1]-1))
    Ub = np.exp(2.5*(hb-1))
    Ud[z<hb] = Ub*np.log((z[z<hb])/z0g) / np.log(hb/z0g)
    Uo = Ud.max()*np.log(z/z0g) / np.log(2/z0g)
    U = (fv*Ud + (1 - fv)*Uo) / Ud.max()
    plt.plot(U,z,'k')

plt.xlim(0,U.max())
plt.ylim(z0g,2)
plt.xticks([0,1])
plt.yticks([z0g,hb,1,2],['$z_0$','$h_b$','$h_c$','$z_U$'])
plt.xlabel('$U/U_a$')
plt.ylabel('Height')
plt.text(0.02,0.9,'canopy')
plt.tight_layout()
plt.savefig('Figure04.pdf')
