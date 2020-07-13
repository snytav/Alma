#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include "Output.h"
#include "World.h"
#include "Species.h"


#using namespace std

#saves fields in VTK format'''
def fields(world, species):
    import numpy as np
    from uvw import RectilinearGrid, DataArray

    # Creating coordinates
    x = np.linspace(-0.5, 0.5, 10)
    y = np.linspace(-0.5, 0.5, 20)
    z = np.linspace(-0.9, 0.9, 30)

    # Creating the file (with possible data compression)
    grid = RectilinearGrid('grid.vtr', (x, y, z), compression=True)

    # A centered ball
    x, y, z = np.meshgrid(x, y, z, indexing='ij')
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    ball = r < 0.3

    # Some multi-component multi-dimensional data
    data = np.zeros([10, 20, 30, 3, 3])
    data[ball, ...] = np.array([[0, 1, 0],
                                [1, 0, 0],
                                [0, 1, 1]])

    # Some cell data
    cell_data = np.zeros([9, 19, 29])
    cell_data[0::2, 0::2, 0::2] = 1

    # Adding the point data (see help(DataArray) for more info)
    grid.addPointData(DataArray(data, range(3), 'ball'))
    # Adding the cell data
    grid.addCellData(DataArray(cell_data, range(3), 'checkers'))
    grid.write()

    # '''species number densities'''
    # for (Species &sp:species)
    #     out<<"<DataArray Name=\"nd."<<sp.name<<"\" NumberOfComponents=\"1\" format=\"ascii\" type=\"Float64\">\n"
    #     out<<sp.den
    #     out<<"</DataArray>\n"
    #
    #
    # '''electric field, component vector'''
    # out<<"<DataArray Name=\"ef\" NumberOfComponents=\"3\" format=\"ascii\" type=\"Float64\">\n"
    # out<<world.ef
    # out<<"</DataArray>\n"
    #
    # '''close out tags'''
    # out<<"</PointData>\n"
    # out<<"</ImageData>\n"
    # out<<"</VTKFile>\n"
    # out.close()


#writes information to the screen
def screenOutput(self, world, species):
    return
#     cout<<"ts: "<<world.getTs()
#     for (Species &sp:species)
#         cout<<setprecision(3)<<"\t "<<sp.name<<":"<<sp.getNp()
#     cout<<endl
#
#
# #file stream handle
# namespace Output
# std.ofstream f_diag


#save runtime diagnostics to a file
def diagOutput(self, world, species):
    return
    # using namespace Output;	#to get access to f_diag
    #
    # #is the file open?
    # if not f_diag.is_open():
    #     f_diag.open("runtime_diags.csv")
    #     f_diag<<"ts,time,wall_time"
    #     for (Species &sp:species)
    #         f_diag<<",mp_count."<<sp.name<<",real_count."<<sp.name
    #               <<",px."<<sp.name<<",py."<<sp.name<<",pz."<<sp.name
    #               <<",KE."<<sp.name
    #     f_diag<<",PE,E_total"<<endl
    #
    #
    # f_diag<<world.getTs()<<","<<world.getTime()
    # f_diag<<","<<world.getWallTime()
    #
    # tot_KE = 0
    # for (Species &sp:species)
    #     KE = sp.getKE();	#species kinetic energy
    #     tot_KE += KE;		#increment total energy
    #     mom = sp.getMomentum()
    #
    #     f_diag<<","<<sp.getNp()<<","<<sp.getRealCount()
    #           <<","<<mom[0]<<","<<mom[1]<<","<<mom[2]<<","<<KE
    #
    #
    # #write out system potential and total energy
    # PE = world.getPE()
    # f_diag<<","<<PE<<","<<(tot_KE+PE)
    #
    # f_diag<<"\n";	#use \n to avoid flush to disc
    # if world.getTs()%25==0) f_diag.flush(:


