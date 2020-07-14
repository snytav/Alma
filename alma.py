import sys

from World import World
from Species import *
from constants import *
from PotentialSolver import PotentialSolver
import numpy as np
import Output
from xml_io_lib import xread



world = World(21, 21, 21)
world.setExtents([-0.1,-0.1,0],[0.1,0.1,0.2])
world.setTime(2e-10,10) # 10000

sp1 = Species("O+", 16*AMU, QE, world)
sp2 = Species("e-", ME, -1*QE, world)
species = [sp1,sp2]

np_ions_grid = np.array([41,41,41])
np_eles_grid = np.array([21,21,21])

species[0].loadParticlesBoxQS(world.getX0(),world.getXm(),1e11,np_ions_grid)	#ions
species[1].loadParticlesBoxQS(world.getX0(),world.getXc(),1e11,np_eles_grid)	#electrons

# initialize potential solver and solve initial potential
solver = PotentialSolver(world,10000,1e-4)
solver.solve()

solver.computeEF()

# main loop
while(world.advanceTime()):
    #move particles
    for sp in species:
        sp.advance()
        sp.computeNumberDensity()

    # compute charge density
    world.computeChargeDensity(species)

    #update potential
    solver.solve()
    Output.fields(world, species)

    #obtain electric field
    solver.computeEF()

    #screen and file output
    #Output.screenOutput(world,species)
    #Output.diagOutput(world,species)
    #
    # periodically write out results
    if world.getTs()%100 == 0 or world.isLastTimeStep():
         Output.fields(world, species)

