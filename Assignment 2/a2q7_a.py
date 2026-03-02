import sympy as sp
x,y=sp.symbols('x y') # Define symbols
T=10-8*x**2-2*y**2
x_min,x_max=0,1
y_min,y_max=0,2
integral=sp.integrate(T,(x,0,1),(y,0,2))
area=(x_max-x_min)*(y_max-y_min)
average_temp=integral/area
print('Average temperature:')
sp.pprint(average_temp)