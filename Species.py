import numpy as np
from particle import Particle
from debug_output import *
from Field import Field

class Species(object):

    def __init__(self,name,mass,charge,world):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.world = world
        self.den = Field(world.ni,world.nj,world.nj,1)


   # returns the number of simulation particles
    def getNp(self):
       return particles.size()

   # returns the number of real particles
    def getRealCount(self):
        return 1.0

   # returns the species momentum
    def getMomentum(self):
        return 1.0

   # returns the species kinetic energy
    def getKE(self):
        return 1.0




   # moves all particles using electric field ef[]
    def advance(self):
        #get the time step
        dt = self.world.getDt()

        #save mesh bounds
        x0 = self.world.getX0()
        xm = self.world.getXm()

        #continue while particles remain
        for part in self.particles:
            #get logical coordinate of particle's position
            lc = self.world.XtoL(part.pos)

            #electric field at particle position
            ef_part = self.world.ef.gather(lc)

            #update velocity from F=qE
            part.vel += ef_part * (dt * self.charge / self.mass)

            #update position from v=dx/dt
            part.pos += part.vel * dt

            #did self particle leave the domain? reflect back
            for i in range(0,3):
                if part.pos[i] < x0[i]:
                    part.pos[i] = 2 * x0[i] - part.pos[i]
                    part.vel[i] *= -1.0

                elif part.pos[i] >= xm[i]:
                    part.pos[i] = 2 * xm[i] - part.pos[i]
                    part.vel[i] *= -1.0

        if self.charge > 0:
            name = 'ions'
        else:
            name = 'electrons'

        writeParticles(self.particles, name, self.world.ts)
        return

   # # compute number density
   #  def computeNumberDensity(self):
   #      den.clear()
   #      for part in self.particles:
   #          lc = world.XtoL(part.pos)
   #          den.scatter(lc, part.mpw)
   #
   #      # divide by node volume
   #      self.den.data =  np.divide(self.den.data,world.node_vol)


   # adds a new particle
    def addParticle(self, pos, vel, mpw):
        # don't do anything (return) if pos outside domain bounds [x0,xd)
        if (not self.world.inBounds(pos)):
            return

        # get particle logical coordinate
        lc = self.world.XtoL(pos)

        # evaluate electric field at particle position
        ef_part = self.world.ef.gather(lc)

        # rewind velocity back by 0.5*dt*ef
        vel -= self.charge / self.mass * ef_part * (0.5 * self.world.getDt())

        return Particle(pos,vel,mpw)    # add to list

    # random load of particles in a x1-x2 box representing num_den number density
    def loadParticlesBox(self,x1,x2,num_den,num_mp):
        return

     
   # quiet start load of particles in a x1-x2 box representing num_den number density
    def loadParticlesBoxQS(self,x1,x2,num_den,num_mp):
        box_vol = np.prod(np.subtract(x2, x1))  # box
        num_mp_tot = np.prod(np.subtract(num_mp, np.ones(3)))  # total number of simulation particles
        num_real = num_den * box_vol  # number of real particles double
        mpw = num_real / num_mp_tot  # macroparticle weight

        # compute particle grid spacing
        d = np.divide(np.subtract(x2, x1), np.subtract(num_mp, np.ones(3)))

        l = []
        # load particles on a equally spaced grid
        for i in range(0, num_mp[0]):
            for j in range(0, num_mp[1]):
                for k in range(0, num_mp[2]):
                    pos = np.add(x1, np.multiply(np.array([i, j, k]), d))

                    # shift particles on max faces back to the domain
                    if abs(pos[0] - x2[0]) < 1e-15: pos[0] -= 1e-4 * d[0]
                    if abs(pos[1] - x2[1]) < 1e-15: pos[1] -= 1e-4 * d[1]
                    if abs(pos[2] - x2[2]) < 1e-15: pos[2] -= 1e-4 * d[2]

                    w = 1;  # relative weight
                    if i == 0 or i == (num_mp[0] - 1): w *= 0.5
                    if j == 0 or j == (num_mp[1] - 1): w *= 0.5
                    if k == 0 or k == (num_mp[2] - 1): w *= 0.5

                    # add rewind
                    vel = np.zeros(3)  # particle is stationary
                    p = self.addParticle(pos, vel, mpw * w)  # add a new particle to the array
                    l.append(p)

        self.particles = l

#TODO: check density evaluation at ts = 1
#      particles OK

    def computeNumberDensity(self):
        self.den.clear()
        if self.charge > 0:
            spname = 'ion'
        else:
            spname = 'el'

        name    = spname + 'NumDens'
        volname = spname + 'VolDens'
        denname = spname + '_den'

        for part in self.particles:
            lc = self.world.XtoL(part.pos)
            self.den.scatter(lc, part.mpw)

        write_3D(self.world, self.den.data, denname, self.world.getTs(), 0)
        write_3D(self.world, self.world.node_vol, volname, self.world.getTs(), 0)

        # divide by node volume
        self.den.data = np.divide(self.den.data,self.world.node_vol)


        write_3D(self.world, self.den.data, name, self.world.getTs(), 0)
        return


