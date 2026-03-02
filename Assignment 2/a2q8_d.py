import sympy as sp
x,y,z,r,t=sp.symbols('x y z r t')
x_expr=2*sp.cos(t)
y_expr=2*sp.sin(t)
z_expr=0
F_x,F_y,F_z=2*z,3*x,5*y
dx=sp.diff(x_expr,t)
dy=sp.diff(y_expr,t)
dz=sp.diff(z_expr,t)
P=F_x*dx+F_y*dy+F_z*dz
integrand1=P.subs({x:x_expr,y:y_expr,z:z_expr})
line_integral=sp.integrate(integrand1,(t,0,2*sp.pi))
print('The line integral:')
sp.pprint(line_integral)

curl_F=sp.Matrix([
    sp.diff(F_z,y)-sp.diff(F_y,z),  
    sp.diff(F_x,z)-sp.diff(F_z,x),  
    sp.diff(F_y,x)-sp.diff(F_x,y) 
])
g=4-x**2-y**2
normal=sp.Matrix([-sp.diff(g,x),-sp.diff(g,y),1])
Q=curl_F.dot(normal)
integrand2=(Q*r).subs({x:x_expr,y:y_expr,z:z_expr})
Surface_integral=sp.integrate(integrand2,(r,0,2),(t,0,2*sp.pi))
print('The surface integral:')
sp.pprint(Surface_integral)

if line_integral==Surface_integral:
    print('\nStoke\'s theorem varified.')
else:
    print('\nStoke\'s theorem is not varified.')