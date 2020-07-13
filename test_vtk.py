import numpy as np
from enthought.tvtk.api import tvtk, write_data

data = np.random.random((10,10,10))

grid = tvtk.ImageData(spacing=(10, 5, -10), origin=(100, 350, 200), 
                      dimensions=data.shape)
grid.point_data.scalars = np.ravel(order='F')
grid.point_data.scalars.name = 'Test Data'

# Writes legacy ".vtk" format if filename ends with "vtk", otherwise
# this will write data using the newer xml-based format.
write_data(grid, 'test.vtk')
