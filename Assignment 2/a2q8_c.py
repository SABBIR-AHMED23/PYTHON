import sympy as sp
x,y,z,r,theta=sp.symbols('x y z r theta') # Define symbols
F=sp.Matrix([x**3, y**3, z**2])
div_F=sum(sp.diff(F[i],var) for i, var in enumerate((x, y, z)))
# In cylindrical coordinates
div_cyl=div_F.subs({x:r*sp.cos(theta), y:r*sp.sin(theta)})

integrand=div_cyl*r
volume_integral=sp.integrate(integrand,(z,0,2),(r,0,3),(theta,0, 2*sp.pi))
print("Flux using Divergence Theorem:")
sp.pprint(volume_integral)