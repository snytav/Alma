import numpy as np

def computeEF(dx,phi,order2):
    for i in range(0,len(phi)):
        ef[i]  = (phi[i+1] - phi[i-1])/dx

    n = len(phi)

    if order2:
        ef[0]    = (3*phi[0]-4*phi[1]+phi[2])/(2*dx)
        ef[ni-1] = (-phi[ni-3]+4*phi[ni-2]-3*phi[ni-1])/(2*dx)
    else:     # first order
        ef[0]    = (phi[0]-phi[1])/dx
        ef[ni-1] = (phi[ni-2]-phi[ni-1])/dx

# uses linear interpolation to evaluate f at li
def gather(li,f):
    i  = int(li)
    di = li-i
    return (f[i]*(1-di) + f[i+1]*(di))


