import numpy as np
from pyvtk import PolyData, VtkData

points = [
    (0, 0, 0),
    (1, 0, 0),
    (0.5, np.sqrt(3)/2, 0),
    (0.5, np.sqrt(3)/6, np.sqrt(3)/2)
]

polygons = [
    [0, 1, 2],
    [0, 1, 3],
    [1, 2, 3],
    [2, 0, 3]
]

structure = PolyData(
    points=points,
    polygons=polygons
)

vtk = VtkData(structure)
vtk.tofile('pyramid', 'ascii')
