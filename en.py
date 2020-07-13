import numpy as np
from constants import *
from poisson import solvePoisson1DExact
from PIC import *
from ElectricField import *

ni = 21    # number of nodes
x0 = 0     #origin
xd = 0.1   # opposite end
dx = (xd - x0) /(ni - 1) # node spacing


rho = np.ones(ni)*QE*1e12
ef  = np.zeros(ni)
phi = np.zeros(ni)

phi = solvePoisson1DExact(dx,rho)

#generate a test electron
m = ME
q = QE
x = 4*dx
v = 0

dt = 1e-10      #timestep

#velocity rewind
li = XtoL(x,dx,x0)
ef_p = gather(li,ef)
v = - 0.5*q/m*ef_p*dt

#save initial potential for PE calculation
phi_max = np.max(phi)

total_timesteps = 4000
out = np.zeros((total_timesteps,5))

for i in range(0,total_timesteps):
    #mesh data at particle position
    li = XtoL(x,dx,x0)
    ef_p = gather(li,ef)

    #integrate velocity and position
    x_old = x
    v += (q/m)*ef_p*dt
    x += v*dt

    phi_p = gather(XtoL(0.5*(x+x_old),dx,x0),phi)     # KE in eV
    ke = 0.5*m*v*v/QE                                 # E in eV
    pe = q*(phi_p-phi_max)/QE                         # PE in eV

    out[i][0] = i*dt
    out[i][1] = x
    out[i][2] = v
    out[i][3] = ke
    out[i][4] = pe
    
np.savetxt('trace.csv', out, delimiter=',', fmt='%15.5e')
