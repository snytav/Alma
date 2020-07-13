import numpy as np
from mayavi.mlab import *

def test_volume_slice():
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]

    scalars = x * x * 0.5 + y * y + z * z * 2.0

    obj = volume_slice(scalars, plane_orientation='x_axes')
    return obj

test_volume_slice()
show()

try:
    engine = mayavi.engine
except NameError:
    from mayavi.api import Engine
    engine = Engine()
    engine.start()
if len(engine.scenes) == 0:
    engine.new_scene()
# ------------------------------------------- 
scene = engine.scenes[0]
scene.scene.show_axes = True
