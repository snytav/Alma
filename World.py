import time
#import _World
import numpy as np
from Field import Field
from constants import *

#import Lib
# @Lib.add_functions_as_methods(
#     (_World.computeChargeDensity))


class World(object):

    def __init__(self,ni,nj,nk):
        """Constructor"""
        self.ni     = ni
        self.nj     = nj
        self.nk     = nk
        self.nn     = np.array([ni,nj,nk])
        self.ef     = Field(ni,nj,nk,3)
        self.phi    = np.zeros((ni,nj,nk))
        self.rho    = np.zeros((ni,nj,nk))
        self.time   = 0.0
        self.dt     = 0.0
        self.ts     = -1  # current time step
        self.num_ts = 0   # number of time steps

    # both parameters are 3D
    def setExtents(self,x0,xm):  
        self.x0 = x0
        self.xm = xm

    def getX0(self):
        return self.x0
            
    def getXm(self):
        return self.xm

    def getXc(self):
        return self.xc

    def getDh(self):
        return self.dh

    def getTs(self):
        return self.ts

    def getTime(self):
        return self.time

    def getWallTime(self):  #returns wall time in seconds
        return time.time()

    def getDt(self):
        return self.dt

    def isLastTimeStep(self):
        return self.ts==self.num_ts-1

    def inBounds(self,pos):
        for i in range(0,3):
            if pos[i]<self.x0[i] or pos[i]>=self.xm[i]:
                return False
        return True
        
    # sets time step and number of time steps*/
    def setTime(self,dt,num_ts):
        self.dt = dt
        self.num_ts=num_ts

    # advances to the next time step, returns true as long as more time steps remain
    def advanceTime(self):
        self.time += self.dt
        self.ts += 1
        return self.ts<= self.num_ts

    # converts physical position to logical coordinate
    def XtoL(self,x):
        return np.divide(np.subtract(x,self.x0),self.dh)

    # computes charge density from rho = sum(charge*den)
    def computeChargeDensity(self,species):
        self.rho = 0
        for sp in species:
            if abs(sp.charge) < abs(QE): continue  # don't bother with neutrals
            self.rho += sp.charge * sp.den.data

    def getPE(self):       # system potential energy
        return _World.getPE(self)

    # advances to the next time step, returns true as long as more time steps remain
    def advance(self):
        self.time += self.dt
        self.ts += 1
        return self.ts <= self.num_ts

    def computeNodeVolumes(self):
        self.node_vol = np.zeros((self.ni,self.nj,self.nk))
        for i in range(0,self.ni):
            for j in range(0,self.nj):
                for k in range(0,self.nk):
                    V = np.prod(self.dh) # default volume
                    if i == 0 or i == self.ni - 1: V *= 0.5 # reduce by two for each boundary index
                    if j == 0 or j == self.nj - 1: V *= 0.5
                    if k == 0 or k == self.nk - 1: V *= 0.5
                    self.node_vol[i][j][k] = V


    def setExtents(self, _x0, _xm):
        #set origin and the opposite corner
        self.x0 = _x0
        self.xm = _xm

        # compute spacing by dividing length by the number of cells
        self.dh = np.divide(np.subtract(self.xm,self.x0),np.subtract(np.array(self.nn),np.ones(3)))

        #compute centroid
        self.xc = 0.5*np.add(self.x0,self.xm)

        #recompute node volumes
        self.computeNodeVolumes()
        return





    

    


    

