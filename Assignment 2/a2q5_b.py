import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# SYMBOLIC COMPUTATION
# Define variables
x, y, z, lam = sp.symbols('x y z lam', real=True)

# Temperature function and constraint (ellipsoid)
T = 600 + 8*x**2 + 4*y**2 - 16*z
g = x**2/4 + y**2/4 + z**2/16 - 1

# Gradients
grad_T = [sp.diff(T, var) for var in (x, y, z)]
grad_g = [sp.diff(g, var) for var in (x, y, z)]

# Lagrange multiplier equations: ∇T = λ∇g
eqs = [
    sp.Eq(grad_T[0], lam * grad_g[0]),
    sp.Eq(grad_T[1], lam * grad_g[1]),
    sp.Eq(grad_T[2], lam * grad_g[2]),
    sp.Eq(g, 0)
]

# Solve the system of equations
solutions = sp.solve(eqs, (x, y, z, lam), dict=True)

# Identify the hottest point
max_T = None
max_point = None
for sol in solutions:
    t_val = T.subs(sol)
    if (max_T is None) or (t_val > max_T):
        max_T = t_val
        max_point = sol

print("Hottest point:", max_point)
print("Maximum temperature:", max_T)

# VISUALIZATION
# Ellipsoid parameterization
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_ell = 2 * np.outer(np.cos(u), np.sin(v))
y_ell = 2 * np.outer(np.sin(u), np.sin(v))
z_ell = 4 * np.outer(np.ones(np.size(u)), np.cos(v))

# Figure setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Ellipsoid surface
ax.plot_surface(x_ell, y_ell, z_ell, color='skyblue', alpha=0.5, linewidth=0, rstride=4, cstride=4)

# Hottest point coordinates
hx = float(max_point[x])
hy = float(max_point[y])
hz = float(max_point[z])
ax.scatter(hx, hy, hz, color='red', s=80, label='Hottest Point')

# Labels and legend
ax.set_xlabel('X-axis', fontsize=10)
ax.set_ylabel('Y-axis', fontsize=10)
ax.set_zlabel('Z-axis', fontsize=10)
ax.set_title('Ellipsoid Surface and Hottest Point', fontsize=12)
ax.legend()
plt.show()
