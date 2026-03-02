import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
t=sp.Symbol('t') # Define the symbol
r=sp.Matrix([3*t, sp.sin(t), t**2])
v=r.diff(t)
a=v.diff(t)
print("Velocity vector:\n")
sp.pprint(v)
print("\nAcceleration vector:\n")
sp.pprint(a)
# Theta(t): angle in x-y plane
theta_expr=sp.atan2(v[1],v[0])
# Numeric function
theta_func=sp.lambdify(t,theta_expr,'numpy')
# Values to plot
t_vals=np.linspace(0,10,500)
theta_vals=theta_func(t_vals)
plt.figure(figsize=(8,4))
plt.plot(t_vals,theta_vals)
plt.xlabel("t")
plt.ylabel(r"$\theta(t)$ $rad$")
plt.grid(True)
plt.show()
