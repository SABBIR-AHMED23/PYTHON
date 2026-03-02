import sympy as sp
x,y,z,t=sp.symbols('x y z t')
f=x*y+z**3
x_expr=sp.cos(t)
y_expr=sp.sin(t)
z_expr=t

dx=sp.diff(x_expr,t)
dy=sp.diff(y_expr,t)
dz=sp.diff(z_expr,t)

ds=sp.sqrt(dx**2+dy**2+dz**2)
integrand=(f*ds).subs({x:x_expr, y:y_expr, z:z_expr})
integral=sp.integrate(integrand,(t,0,sp.pi))
print('The line integral is:')
sp.pprint(integral)