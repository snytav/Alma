import numpy as np

class Field(object):

    def __init__(self,ni,nj,nk,dim):
        self.ni   = ni
        self.nj   = nj
        self.nk   = nk
        self.dim  = dim
        if dim > 1:
           self.data = np.zeros((ni,nj,nk,dim))
        else:
            self.data = np.zeros((ni, nj, nk))

    def clear(self):
        if self.dim > 1:
            self.data = np.zeros((self.ni, self.nj, self.nk, self.dim))
        else:
            self.data = np.zeros((self.ni, self.nj, self.nk))


    # scatters scalar value onto a field at logical coordinate lc'''
    def scatter(self,lc, value):
        i  = int(lc[0])
        di = lc[0]-i

        j  = int(lc[1])
        dj = lc[1]-j

        k  = int(lc[2])
        dk = lc[2]-k

        self.data[i][j][k]       += value*(1-di)*(1-dj)*(1-dk)
        self.data[i+1][j][k]     += value*(di)*(1-dj)*(1-dk)
        self.data[i+1][j+1][k]   += value*(di)*(dj)*(1-dk)
        self.data[i][j+1][k]     += value*(1-di)*(dj)*(1-dk)
        self.data[i][j][k+1]     += value*(1-di)*(1-dj)*(dk)
        self.data[i+1][j][k+1]   += value*(di)*(1-dj)*(dk)
        self.data[i+1][j+1][k+1] += value*(di)*(dj)*(dk)
        self.data[i][j+1][k+1]   += value*(1-di)*(dj)*(dk)


    # gathers field value at logical coordinate lc'''
    def gather(self,lc):
        i  = int(lc[0])
        di = lc[0]-i

        j  = int(lc[1])
        dj = lc[1]-j

        k  = int(lc[2])
        dk = lc[2]-k

        #gather electric field onto particle position'''
        val = (self.data[i][j][k]*(1-di)*(1-dj)*(1-dk)+
        self.data[i+1][j][k]*(di)*(1-dj)*(1-dk)+
        self.data[i+1][j+1][k]*(di)*(dj)*(1-dk)+
        self.data[i][j+1][k]*(1-di)*(dj)*(1-dk)+
        self.data[i][j][k+1]*(1-di)*(1-dj)*(dk)+
        self.data[i+1][j][k+1]*(di)*(1-dj)*(dk)+
        self.data[i+1][j+1][k+1]*(di)*(dj)*(dk)+
        self.data[i][j+1][k+1]*(1-di)*(dj)*(dk))

        return val



