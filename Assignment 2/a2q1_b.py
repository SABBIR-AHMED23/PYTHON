import sympy as sp
# Normals
n1=sp.Matrix([3,-6,-2])
n2=sp.Matrix([2,1,-2])
# Cross product
direction=n1.cross(n2)
print("Vector parallel to the intersection line:")
sp.pprint(direction)