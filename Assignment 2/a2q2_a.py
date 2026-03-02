import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
t=sp.Symbol('t') # Define symbolic variable
# Parametric curve
r=sp.Matrix([5*sp.cos(t), 4*sp.sin(t)])
r_prime=r.diff(t)  # Derivative
# Evaluation points
t1=sp.pi/4
t2=sp.pi
# Compute position vectors
r_t1=r.subs(t,t1)
r_t2=r.subs(t,t2)
# Compute tangent vectors
r_prime_t1=r_prime.subs(t,t1)
r_prime_t2=r_prime.subs(t,t2)
# Display symbolic tangent vectors
print("\nTangent vector at t=pi/4:")
sp.pprint(r_prime_t1)
print("\nTangent vector at t=pi:")
sp.pprint(r_prime_t2)
# Numeric functions for plotting
x_func=sp.lambdify(t,r[0],'numpy')
y_func=sp.lambdify(t,r[1],'numpy')
# Generate points on the curve
t_vals=np.linspace(0,2*np.pi, 400)
x_vals=x_func(t_vals)
y_vals=y_func(t_vals)
# Convert symbolic values to numeric arrays
r1=np.array([float(r_t1[0].evalf()), float(r_t1[1].evalf())])
r2=np.array([float(r_t2[0].evalf()), float(r_t2[1].evalf())])
v1=np.array([float(r_prime_t1[0].evalf()), float(r_prime_t1[1].evalf())])
v2=np.array([float(r_prime_t2[0].evalf()), float(r_prime_t2[1].evalf())])
# Plot the curve
plt.figure(figsize=(8,8))
plt.plot(x_vals, y_vals,'b',label='Curve C')
# Plot position vectors from origin
plt.quiver(0,0,r1[0],r1[1],angles='xy',scale_units='xy',scale=1,color='g',label='r(pi/4)')
plt.quiver(0,0,r2[0],r2[1],angles='xy',scale_units='xy',scale=1,color='c',label='r(pi)')
# Plot tangent vectors at those points
plt.quiver(r1[0],r1[1],v1[0],v1[1],angles='xy',scale_units='xy',scale=1,color='r',label="r'(pi/4)")
plt.quiver(r2[0],r2[1],v2[0],v2[1],angles='xy',scale_units='xy',scale=1,color='m',label="r'(pi)")
# Formatting the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve C with Position and Tangent Vectors')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()