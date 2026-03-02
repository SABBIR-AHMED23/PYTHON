import sympy as sp
x,y,r,theta=sp.symbols('x y r theta') # Define variables
# Define vector field components
f=sp.exp(x)-y**3
g=sp.cos(y)+x**3
# Compute partial derivatives for Green's Theorem
dg_dx=sp.diff(g,x)
df_dy=sp.diff(f,y)
curl=dg_dx-df_dy
# Substitute x=rcosθ, y=rsinθ
x_sub=r*sp.cos(theta)
y_sub=r*sp.sin(theta)
curl_polar=curl.subs({x:x_sub, y:y_sub})

integrand=curl_polar*r # dxdy=rdrd0
# Perform double integration
result=sp.integrate(integrand,(r,0,1),(theta,0,2*sp.pi))
print("Work done using Green's Theorem:")
sp.pprint(result)
