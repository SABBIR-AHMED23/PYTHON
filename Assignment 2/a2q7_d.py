import sympy as sp
x,y=sp.symbols('x y') # Define symbols
Fx=sp.exp(y)
Fy=x*sp.exp(y)
# (i) Check if conservative
dFy_dx=sp.diff(Fy,x)
dFx_dy=sp.diff(Fx,y)
is_conservative=sp.simplify(dFy_dx-dFx_dy)==0
print("Is conservative?", is_conservative)

# (ii) Find potential function φ
phi_x=sp.exp(y)
phi_y=x*sp.exp(y)
g_x=sp.Function('g')(x)
phi=sp.integrate(phi_y,y)+g_x
phi_x_=sp.diff(phi,x)
simplify=phi_x_-phi_x
g_val=sp.integrate(simplify,x)
g_=sp.solve(g_val,g_x)
phi_final=phi.subs(g_x,g_[0])
print("Potential function φ(x, y):", phi_final)

# (iii) Work done along path from (1,0) to (-1,0)
W=phi_final.subs({x:-1, y:0})-phi_final.subs({x:1, y:0})
print("Work done along path C:", W)