import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
t=sp.Symbol('t',real=True) # Define t as a symbol 
def compute_frenet(r,t):
    r_prime=r.diff(t)
    r_double_prime=r_prime.diff(t)
    r_triple_prime=r_double_prime.diff(t)

    T=r_prime/sp.sqrt(r_prime.dot(r_prime))
    T_prime=T.diff(t)
    N=T_prime/sp.sqrt(T_prime.dot(T_prime))
    B=T.cross(N)
    kappa=r_prime.cross(r_double_prime).norm()/r_prime.norm()**3
    tau=r_prime.cross(r_double_prime).dot(r_triple_prime)/r_prime.cross(r_double_prime).norm()**2
    return T,N,B,kappa,tau
r1=sp.Matrix([sp.exp(t), sp.exp(t)*sp.cos(t), sp.exp(t)*sp.sin(t)])
T1,N1,B1,kappa1,tau1=compute_frenet(r1,t)
print("First Curve: Evaluation at t=0")
T1_0=T1.subs(t,0)
N1_0=N1.subs(t,0)
B1_0=B1.subs(t,0)
kappa1_0=kappa1.subs(t,0)
tau1_0=tau1.subs(t,0)
print("Tangent vector T1(t):\n")
sp.pprint(T1_0.T)
print("Normal vector N1(t):\n")
sp.pprint(N1_0.T)
print("Binormal vector B1(t):\n")
sp.pprint(B1_0.T)
print("Curvature κ1(t):\n")
sp.pprint(kappa1_0)
print("Torsion τ1(t):\n")
sp.pprint(tau1_0)

r2=sp.Matrix([2*sp.cos(t), 3*sp.sin(t), 0])
T2,N2,B2,kappa2,tau2=compute_frenet(r2,t)

print("\n\nSecond Curve:")
print("Tangent vector T2(t):\n")
sp.pprint(sp.simplify(T2).T)
print("\nNormal vector N2(t):\n")
sp.pprint(sp.simplify(N2).T)
print("\nBinormal vector B2(t):\n")
sp.pprint(sp.simplify(B2).T)
print("\nCurvature κ2(t):\n")
sp.pprint(sp.simplify(kappa2))
print("\nTorsion τ2(t):\n")
sp.pprint(sp.simplify(tau2))
# For plotting curvature
kappa1_func=sp.lambdify(t,kappa1,"numpy")
kappa2_func=sp.lambdify(t,kappa2,"numpy")
t_vals=np.linspace(0,2*np.pi,400)
kappa1_vals=kappa1_func(t_vals)
kappa2_vals=kappa2_func(t_vals)

plt.figure(figsize=(8,4))
plt.plot(t_vals,kappa1_vals, label=r'$k_1(t)$')
plt.plot(t_vals,kappa2_vals, label=r'$k_2(t)$')
plt.xlabel("t")
plt.ylabel("Curvature κ(t)")
plt.grid(True)
plt.legend()
plt.show()