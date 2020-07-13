import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from constants import *

ni = 21               # number of nodes
x0 = 0.0              # mesh origin
xm = 0.1              # opposite end
dx = (xm - x0)/(ni-1) # node spacing

phi = np.zeros(ni)
rho = np.ones(ni)*QE*1e12

ef  = np.zeros(ni)

#matrix for Poisson equation
a = -2*np.ones(ni)
A = np.diag(a)
b = np.ones(ni-1)
A = A+np.diag(b,1)+np.diag(b,-1)
A = A

#solution
ia = inv(A)
phi = - ia.dot(rho*dx*dx)
plt.plot(phi)
plt.show()



