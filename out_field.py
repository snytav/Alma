from tvtk.api import tvtk, write_data
import numpy as np

#data = np.random.random((3, 3, 3))
#
#i = tvtk.ImageData(spacing=(1, 1, 1), origin=(0, 0, 0))
#i.point_data.scalars = data.ravel()
#i.point_data.scalars.name = 'scalars'
#i.dimensions = data.shape
#
#w = tvtk.XMLImageDataWriter(input=i, file_name='spoints3d.vti')
#w.write()

points = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0]], 'f')
(n1, n2)  = points.shape
poly_edge = np.array([[0,1,2,3]])

print (n1, n2)
## Scalar Data
#temperature = np.array([10., 20., 30., 40.])
#pressure = np.random.rand(n1)
#
## Vector Data
#velocity = np.random.rand(n1,n2)
#force     = np.random.rand(n1,n2)
#
##Tensor Data with 
comp = 5
stress = np.random.rand(n1,comp)
#
#print stress.shape
## The TVTK dataset.
mesh = tvtk.PolyData(points=points, polys=poly_edge)
#
## Data 0 # scalar data
#mesh.point_data.scalars = temperature
#mesh.point_data.scalars.name = 'Temperature'
#
## Data 1 # additional scalar data
#mesh.point_data.add_array(pressure)
#mesh.point_data.get_array(1).name = 'Pressure'
#mesh.update()
#
## Data 2 # Vector data
#mesh.point_data.vectors = velocity
#mesh.point_data.vectors.name = 'Velocity'
#mesh.update()
#
## Data 3 additional vector data
#mesh.point_data.add_array( force)
#mesh.point_data.get_array(3).name = 'Force'
#mesh.update()

mesh.point_data.tensors = stress
mesh.point_data.tensors.name = 'Stress'

# Data 4 additional tensor Data
#mesh.point_data.add_array(stress)
#mesh.point_data.get_array(4).name = 'Stress'
#mesh.update()

write_data(mesh, 'polydata.vtk')

# XML format 
# Method 1
#write_data(mesh, 'polydata')

# Method 2
#w = tvtk.XMLPolyDataWriter(input=mesh, file_name='polydata.vtk')
#w.write()
sh
