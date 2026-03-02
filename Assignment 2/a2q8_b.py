import sympy as sp
phi,theta=sp.symbols('phi theta') # Define variables
a=1
x=a*sp.sin(phi)*sp.cos(theta)
y=a*sp.sin(phi)*sp.sin(theta)
z=a*sp.cos(phi)
# dS=a^2 sin(phi) dphi dtheta
dS=a**2*sp.sin(phi)
integrand=x**2*dS
surface_integral=sp.integrate(integrand,(theta,0, 2*sp.pi),(phi,0, sp.pi))
print("Surface integral over sphere:")
sp.pprint(surface_integral)
