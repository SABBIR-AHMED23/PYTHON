import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x,y=sp.symbols('x y',real=True) # Define symbols
def is_real_point(point): # Check if all values in point are real
    return all(sp.im(val)==0 for val in point.values())

def classify_critical_point(fxx,fyy,fxy,point):
    fxx_val=fxx.subs(point)
    fyy_val=fyy.subs(point)
    fxy_val=fxy.subs(point)
    D=fxx_val*fyy_val-fxy_val**2
    if not D.is_real:
        return "Complex"
    if D>0:
        if fxx_val>0:
            return "Local Min"
        else:
            return "Local Max"
    elif D<0:
        return "Saddle Point"
    else:
        return "Inconclusive"

def analyze_function(f_expr,name):
    print(f"\n Analyzing: {name}")
    fx=sp.diff(f_expr,x)
    fy=sp.diff(f_expr,y)
    fxx=sp.diff(fx,x)
    fyy=sp.diff(fy,y)
    fxy=sp.diff(fx,y)
    critical_pts=sp.solve([fx, fy],(x,y),dict=True)
    results=[]
    for pt in critical_pts:
        if is_real_point(pt):
            kind=classify_critical_point(fxx,fyy,fxy,pt)
            results.append((pt,kind))
            print(f"Point: {pt} \u2192 {kind}")
        else:
            print(f"Skipped complex point: {pt}")
    return results
# (i)
f1=4*x*y-x**4-y**4
results1=analyze_function(f1, "f(x,y)= 4xy-x^4 -y^4")
# (ii)
f2=4*x**2*sp.exp(y)-2*x**4 -sp.exp(4*y)
results2=analyze_function(f2, "f(x,y)=4x²eʸ-2x⁴-e⁴ʸ")
# Plotting
x_vals=np.linspace(-2,2,300)
y_vals=np.linspace(-2,2,300)
X,Y=np.meshgrid(x_vals,y_vals)
fig=plt.figure(figsize=(12,5))
# Plot (i)
ax1=fig.add_subplot(1,2,1,projection='3d')
Z1=4*X*Y-X**4-Y**4
ax1.plot_surface(X,Y,Z1,cmap='coolwarm',alpha=0.9)
ax1.set_title("f(x, y)= 4xy - x⁴ - y⁴")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("f(x,y)")
# Plot (ii)
ax2=fig.add_subplot(1,2,2,projection='3d')
Z2=4*X**2*np.exp(Y)-2*X**4-np.exp(4*Y)
ax2.plot_surface(X,Y,Z2,cmap='viridis',alpha=0.9)
ax2.set_title("f(x,y)= 4x²eʸ- 2x⁴- e⁴ʸ")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("f(x, y)")
plt.tight_layout()
plt.show()