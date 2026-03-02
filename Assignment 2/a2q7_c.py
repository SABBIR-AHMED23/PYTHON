import sympy as sp
r,h,theta,z=sp.symbols('r h theta z',real=True,positive=True) # Define symbols
# Density function in polar coordinates
rho=r**2
integrand=rho*r # dxdy=rdr dtheta

R,H=sp.symbols('R H',real=True,positive=True)
mass=sp.integrate(integrand,(r,0,R),(theta,0,2*sp.pi),(z,0,H))

mass=sp.simplify(mass)
sp.pprint(mass)