import sympy as sp
x,y=sp.symbols('x,y')
Z=sp.sqrt(4-x**2)
Zx=sp.diff(Z,x)
Zy=sp.diff(Z,y)
integrand=sp.sqrt(Zx**2+Zy**2+1)
surafce_area=sp.integrate(integrand,(x,0,1),(y,0,4))
sp.pprint(surafce_area)