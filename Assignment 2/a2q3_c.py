import sympy as sp
theta,x,y,z=sp.symbols('theta x y z',real=True) # Define symbols
w=sp.sqrt(x**2+y**2+z**2) # Define w
# Partial derivatives
dw_dx=sp.diff(w,x)
dw_dy=sp.diff(w,y)
dw_dz=sp.diff(w,z)
# Define x,y,z
x_expr=sp.cos(theta)
y_expr=sp.sin(theta)
z_expr=sp.tan(theta)
# Derivatives of x,y,z w.r.t theta
dx_dtheta=sp.diff(x_expr,theta)
dy_dtheta=sp.diff(y_expr,theta)
dz_dtheta=sp.diff(z_expr,theta)
# Chain rule
dw_dtheta=dw_dx*dx_dtheta+ dw_dy*dy_dtheta+ dw_dz*dz_dtheta
dw_substituted=dw_dtheta.subs({x:x_expr, y:y_expr, z:z_expr})
print("dw/dtheta:")
sp.pprint(sp.simplify(dw_substituted))
# Evaluate at theta= pi/4
value=dw_substituted.subs(theta, sp.pi/4).evalf()
print("\ndw/dtheta at theta=π/4:")
print(value)