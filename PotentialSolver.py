from World import World
import constants
from math import sqrt
from debug_output import write_3D
import numpy as np

class PotentialSolver(object):
    # constructor, sets world
    def __init__(self, world,max_it,tol):
        self.world         = world
        self.max_solver_it = max_it
        self.tolerance     = tol

     # solves potential using Gauss - Seidel
    def solve(self):
        # references to avoid having to write world.phi
        phi = self.world.phi
        rho = self.world.rho

        # precompute 1/(dx^2)
        dh = self.world.getDh()
        idx2 = 1.0 / (dh[0] * dh[0])
        idy2 = 1.0 / (dh[1] * dh[1])
        idz2 = 1.0 / (dh[2] * dh[2])

        L2 = 0  # norm
        converged = False
        # rho OK for step 1,2
        write_3D(self.world, rho, 'rho', self.world.getTs(),0)
        phi_new = np.zeros((self.world.ni,self.world.nj,self.world.nk))

        '''solve potential'''
        for it in range(0, self.max_solver_it):
            for i in range(1, self.world.ni-1):
                for j in range(1, self.world.nj-1):
                    for k in range(1, self.world.nk-1):
                        # standard internal open node
                        phi_new = (rho[i][j][k] / constants.EPS_0 +
                                   idx2 * (phi[i - 1][j][k] + phi[i + 1][j][k]) +
                                   idy2 * (phi[i][j - 1][k] + phi[i][j + 1][k]) +
                                   idz2 * (phi[i][j][k - 1] + phi[i][j][k + 1])) / (2 * idx2 + 2 * idy2 + 2 * idz2)

                        '''SOR'''
                        phi[i][j][k] = phi[i][j][k] + 1.4 * (phi_new - phi[i][j][k])
# 200 iters
            write_3D(self.world,phi, 'phi', self.world.getTs(), it)

            #check for convergence
            if it % 25 == 0:
                sum = 0
                for i in range(1, self.world.ni-1):
                    for j in range(1, self.world.nj-1):
                        for k in range(1, self.world.nk-1):
                            R =( -phi[i][j][k] * (2 * idx2 + 2 * idy2 + 2 * idz2) +
                            rho[i][j][k] / constants.EPS_0 +
                            idx2 * (phi[i - 1][j][k] + phi[i + 1][j][k]) +
                            idy2 * (phi[i][j - 1][k] + phi[i][j + 1][k]) +
                            idz2 * (phi[i][j][k - 1] + phi[i][j][k + 1]) )

                            sum += R * R

            L2 = sqrt(sum / (self.world.ni * self.world.nj * self.world.nk))
            if L2 < self.tolerance:
                converged = True
                break

        #ph at timestep 2-6 OK
        write_3D(self.world, phi, 'phiconv', self.world.getTs(), it)

        if (not converged):
            print('failed to converge, L2 = ',L2)
        return converged

    # *computes electric field = -gradient(phi)
    def computeEF(self):
        # reference to phi to avoid needing to write world.phi
        phi = self.world.phi

        dh = self.world.getDh()
        dx = dh[0]
        dy = dh[1]
        dz = dh[2]

        for i in range(0, self.world.ni):
            for j in range(0, self.world.nj):
                for k in range(0, self.world.nk):
                    ef = self.world.ef.data[i][j][k]  # reference to (i,j,k) ef vec3

                    # '''x component'''
                    if i == 0:  # forward
                        ef[0] = -(-3 * phi[i][j][k] + 4 * phi[i + 1][j][k] - phi[i + 2][j][k]) / (2 * dx)
                    elif i == self.world.ni - 1:  # backward
                        ef[0] = -(phi[i - 2][j][k] - 4 * phi[i - 1][j][k] + 3 * phi[i][j][k]) / (2 * dx)
                    else:  # central
                        ef[0] = -(phi[i + 1][j][k] - phi[i - 1][j][k]) / (2 * dx)

                    # y component
                    if j == 0:
                        ef[1] = -(-3 * phi[i][j][k] + 4 * phi[i][j + 1][k] - phi[i][j + 2][k]) / (2 * dy)
                    elif j == self.world.nj - 1:
                        ef[1] = -(phi[i][j - 2][k] - 4 * phi[i][j - 1][k] + 3 * phi[i][j][k]) / (2 * dy)
                    else:
                        ef[1] = -(phi[i][j + 1][k] - phi[i][j - 1][k]) / (2 * dy)

                    # '''z component'''
                    if k == 0:
                        ef[2] = -(-3 * phi[i][j][k] + 4 * phi[i][j][k + 1] - phi[i][j][k + 2]) / (2 * dz)
                    elif k == self.world.nk - 1:
                        ef[2] = -(phi[i][j][k - 2] - 4 * phi[i][j][k - 1] + 3 * phi[i][j][k]) / (2 * dz)
                    else:
                        ef[2] = -(phi[i][j][k + 1] - phi[i][j][k - 1]) / (2 * dz)

