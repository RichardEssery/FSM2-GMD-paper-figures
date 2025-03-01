"""
A Flexible Snow Model (FSM 2.1.1) including a forest canopy
Figure 3. Canopy albedo and transmission of diffuse and direct-beam shortwave radiation calculated
using Beer's Law and the two-stream approximation in 10,000 simulations with randomly selected values
of $\alpha$ (0.1 - 0.8), $\theta$ (5 - 85$^\circ$), $f_{cs}$ (0 - 1) and $\Lambda$ (0 - 10).
Green points are from simulations with snow-free canopies.
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

plt.rcParams['font.size'] = 20
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.figure(figsize=(12,12))

def bulk(agnd,elev,fcans,LAI,Sdif,Sdir):
    acn0 = 0.1
    acns = 0.3
    acan = (1 - fcans)*acn0 + fcans*acns
    tdif = np.exp(-0.8*LAI)
    tdir = np.exp(-0.5*LAI/np.sin(elev))
    rdif = (1 - tdif)*acan
    rdir = (1 - tdir)*acan
    Sup1 = agnd*(tdif*Sdif + tdir*Sdir)/(1 - agnd*rdif)
    Sdn1 = tdif*Sdif + rdif*Sup1
    Sup0 = rdif*Sdif + rdir*Sdir + tdif*Sup1
    alb = Sup0/(Sdif + Sdir) 
    tau = (Sdn1 + tdir*Sdir)/(Sdif + Sdir)
    return alb,tau 

def canel(agnd,elev,fcans,LAI,Sdif,Sdir):
    avg0 = 0.27
    avgs = 0.65
    aveg = (1 - fcans)*avg0 + fcans*avgs
    omega = aveg
    beta = 0.67
    g1 = 2*(1 - (1 - beta)*omega)
    g2 = 2*beta*omega
    k = np.sqrt(g1**2 - g2**2)
    t = 0.5*LAI
    D = k + g1 + (k - g1)*np.exp(-2*k*t)
    rdif = (g2/D)*(1 - np.exp(-2*k*t))
    tdif = 2*(k/D)*np.exp(-k*t)
    mu = np.sin(elev)
    beta0 = (0.5 + mu)*(1 - mu*np.log((1 + mu)/mu))
    g3 = beta0
    g4 = 1 - beta0
    a1 = g1*g4 + g2*g3
    a2 = g1*g3 + g2*g4
    d = (1 - k**2*mu**2)*((k + g1)*np.exp(k*t) + (k - g1)*np.exp(-k*t))
    b1 = (1 - k*mu)*(a2 + k*g3)*np.exp(k*t)
    b2 = (1 + k*mu)*(a2 - k*g3)*np.exp(-k*t)
    b3 = 2*k*(g3 - a2*mu)*np.exp(-t/mu)
    rdir = (omega/d)*(b1 - b2 - b3)
    b1 = (1 + k*mu)*(a1 + k*g4)*np.exp(k*t)
    b2 = (1 - k*mu)*(a1 - k*g4)*np.exp(-k*t)
    b3 = 2*k*(g4 + a1*mu)*np.exp(t/mu)
    tdir = np.exp(-t/mu)
    fdir = np.exp(-t/mu)*(omega/d)*(b2 + b3 - b1)
    Sup1 = agnd*(tdif*Sdif + (tdir + fdir)*Sdir)/(1 - agnd*rdif)
    Sdn1 = tdif*Sdif + rdif*Sup1 + fdir*Sdir
    Sup0 = rdif*Sdif + rdir*Sdir + tdif*Sup1
    alb = Sup0/(Sdif + Sdir) 
    tau = (Sdn1 + tdir*Sdir)/(Sdif + Sdir)
    return alb,tau

n = 10000
agnd = 0.1 + 0.7*np.random.rand(n)
fcans = np.random.rand(n)
f = 0.0002
SVF = f + (1-f)*np.random.rand(n)
LAI = -np.log(SVF)/0.8
elev = np.deg2rad(10 + 70*np.random.rand(n))

Sdif = 1
Sdir = 0
alb_blk, tau_blk = bulk(agnd,elev,fcans,LAI,Sdif,Sdir)
alb_can, tau_can = canel(agnd,elev,fcans,LAI,Sdif,Sdir)
alb_blk0, tau_blk0 = bulk(agnd,elev,0,LAI,Sdif,Sdir)
alb_can0, tau_can0 = canel(agnd,elev,0,LAI,Sdif,Sdir)
ax = plt.subplot(221)
ax.plot(alb_blk,alb_can,'ko',ms=1)
ax.plot(alb_blk0,alb_can0,'go',ms=1)
ax.plot([0,1],[0,1],'grey',lw=1)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.set_xlabel("Beer's law")
ax.set_ylabel('Two-stream approximation')
ax.set_title('(a) Diffuse albedo')
ax = plt.subplot(222)
ax.plot(tau_blk,tau_can,'ko',ms=1)
ax.plot(tau_blk0,tau_can0,'go',ms=1)
ax.plot([0,1],[0,1],'grey',lw=1)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.set_xlabel("Beer's law")
ax.set_ylabel('Two-stream approximation')
ax.set_title('(b) Diffuse transmission')

Sdif = 0
Sdir = 1
alb_blk, tau_blk = bulk(agnd,elev,fcans,LAI,Sdif,Sdir)
alb_can, tau_can = canel(agnd,elev,fcans,LAI,Sdif,Sdir)
alb_blk0, tau_blk0 = bulk(agnd,elev,0,LAI,Sdif,Sdir)
alb_can0, tau_can0 = canel(agnd,elev,0,LAI,Sdif,Sdir)
ax = plt.subplot(223)
ax.plot(alb_blk,alb_can,'ko',ms=1)
ax.plot(alb_blk0,alb_can0,'go',ms=1)
ax.plot([0,1],[0,1],'grey',lw=1)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.set_xlabel("Beer's law")
ax.set_ylabel('Two-stream approximation')
ax.set_title('(c) Direct-beam albedo')
ax = plt.subplot(224)
ax.plot(tau_blk,tau_can,'ko',ms=1)
ax.plot(tau_blk0,tau_can0,'go',ms=1)
ax.plot([0,1],[0,1],'grey',lw=1)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.set_xlabel("Beer's law")
ax.set_ylabel('Two-stream approximation')
ax.set_title('(d) Direct-beam transmission')

plt.tight_layout()
plt.savefig('Figure03',dpi=400)


