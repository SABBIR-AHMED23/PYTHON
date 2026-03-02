import sympy as sp
t=sp.Symbol('t') # Define t as a symbol
# First curve
r1=sp.Matrix([sp.ln(t), sp.exp(-t), t**3])
r1_prime=r1.diff(t) # Derivative
t0_1=2
r1_at_t0=r1.subs(t,t0_1)
r1_prime_at_t0=r1_prime.subs(t,t0_1)

print("First Curve:")
L1=r1_at_t0+sp.Symbol('lambda')*r1_prime_at_t0
print("Parametric equations of the tangent line:\n")
sp.pprint(L1)

# Second curve
r2=sp.Matrix([2*sp.cos(sp.pi*t), 2*sp.sin(sp.pi*t), 3*t])
r2_prime=r2.diff(t) # Derivative
t0_2=sp.Rational(1,3)
r2_at_t0=r2.subs(t,t0_2)
r2_prime_at_t0=r2_prime.subs(t,t0_2)

print("\n\nSecond Curve:")
L2=r2_at_t0+sp.Symbol('lambda')*r2_prime_at_t0
print("Parametric equations of the tangent line:\n")
sp.pprint(L2)
