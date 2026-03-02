import sympy as sp
x,y,r,t=sp.symbols('x y r t')

x=1+sp.cos(t)
y=sp.sin(t)
z=4-x**2-y**2
intregrand=z*r
result=sp.integrate(intregrand,(r,0,1),(t,0,2*sp.pi))
print('The volume of the solid is:')
sp.pprint(result)