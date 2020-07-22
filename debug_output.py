from particle import Particle


def write_3D(world,field,name,n_timestep,n_iter):
    fname = 'py_'+name+ '_' + str(n_timestep) + '_'+str(n_iter) +'.txt'

    f = open(fname, 'wt')

    for i in range(0,world.ni):
        for j in range(0,world.nj):
            for k in range(0,world.nk):
                f.write("%10d %10d %10d  %15.15e \n" % (i,j,k,field[i][j][k]))

    f.close()
    return

def writeParticles(particles,name,n_timestep):
    fname = 'pypart_' + name + '_' + str(n_timestep) + '_' + '.txt'
    f = open(fname, 'wt')
    for p in particles:
        f.write("%30.20e %30.20e %30.20e %30.20e %30.20e %30.20e \n" % (p.pos[0],p.pos[1],p.pos[2],p.vel[0],p.vel[1],p.vel[2]))

    f.close()
    return
