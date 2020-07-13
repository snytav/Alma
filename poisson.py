import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv



def solvePoisson1DExact(dx,rho):
    ni = len(rho)

    # matrix for Poisson equation
    a = -2*np.ones(ni)
    A = np.diag(a)
    b = np.ones(ni-1)
    A = A+np.diag(b,1)+np.diag(b,-1)

    #solution
    ia = inv(A)
    phi = - ia.dot(rho*dx*dx)
    plt.plot(phi)
    plt.title('1D Poisson solution')
    plt.show()
    return phi


#ni = 20
#dx = 0.1/ni
#rho = np.ones(ni)
#solvePoisson1DExact(dx,rho)
