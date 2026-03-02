import sympy as sp
x,y=sp.symbols('x,y')
f=y**2*sp.cos(x-y) # Define the function
f_xx=sp.diff(f,x,x)
f_yy=sp.diff(f,y,y)
if f_xx+f_yy==0:
    print('Satisty the laplace equation')
else:
    print('Do not satisfy the laplace equation')
#Check CRE
u=f
v=0 # Imaginary part is zero
u_x=sp.diff(u,x)
u_y=sp.diff(u,y)
v_x=sp.diff(v,x)
v_y=sp.diff(v,y)
print('Do Cauchy-Riemann equation hols? ',u_x.equals(v_y) and u_y.equals(-v_x))
#Compute mixed derivatives
f_xy=sp.diff(f,x,y)
f_yx=sp.diff(f,y,x)
print('Are f_xy and f_yx equal? ',f_xy.equals(f_yx))