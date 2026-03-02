import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x,y,z=sp.symbols('x y z') 
f=x**2+ 4*y**2+ z**2- 18 # Define ellipsoid function
point=(1,2,1)
# Gradient of f
grad_f=[sp.diff(f,x),sp.diff(f,y),sp.diff(f,z)]
grad_at_point=[g.subs({x:1,y:2,z:1}) for g in grad_f]

# (i) Tangent Plane Equation
A,B,C=grad_at_point
x0,y0,z0=point
tangent_plane=A*(x-x0)+B*(y-y0)+C*(z-z0)
tangent_plane_eq=sp.Eq(tangent_plane,0)
print("(i) Tangent Plane Equation at (1,2,1):")
sp.pprint(tangent_plane_eq)

# (ii) Parametric equations of the normal line
t=sp.Symbol('t')
normal_line={
    'x(t)': x0 +A*t,
    'y(t)': y0 +B*t,
    'z(t)': z0 +C*t
}
print("\n(ii) Parametric Equations of Normal Line:")
for key, expr in normal_line.items():
    print(f"{key}= {expr}")

# (iii) Acute angle with xy-plane(Angle between normal vector and z-axis)
normal_vector=np.array([float(A),float(B),float(C)])
z_axis=np.array([0,0,1])
cos_theta=np.dot(normal_vector,z_axis)/(np.linalg.norm(normal_vector)*1)
theta_rad=np.arccos(np.abs(cos_theta)) 
theta_deg=np.degrees(theta_rad)
print(f"\n(iii) Acute angle with XY-plane: {theta_deg:.2f} degrees")

# (iv) Visualization
fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111,projection='3d')
# Plot ellipsoid surface
u=np.linspace(0,2*np.pi,50)
v=np.linspace(0,np.pi,50)
X=2 * np.outer(np.cos(u), np.sin(v))
Y = np.sqrt(2) * np.outer(np.sin(u), np.sin(v))
Z = np.sqrt(18) * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(X, Y, Z, color='cyan', alpha=0.4, rstride=4, cstride=4, edgecolor='gray')

# Plot point
ax.scatter(*point,color='red', s=50,label='Point(1,2,1)')
# Plot normal line
t_vals=np.linspace(-1,1,10)
line_x=x0+float(A)*t_vals
line_y=y0+float(B)*t_vals
line_z=z0+float(C)*t_vals
ax.plot(line_x,line_y,line_z,color='black',label='Normal Line')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Ellipsoid, Tangent Point, and Normal Line")
plt.show()