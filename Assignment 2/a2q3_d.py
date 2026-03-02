import numpy as np
import matplotlib.pyplot as plt
#Define the function
def T(x,y):
    return 3*x**2*y
def gradient_T(x,y):
    dT_dx=6*x*y
    dT_dy=3*x**2
    return np.array([dT_dx,dT_dy])
#Compute directional derivative 
def directional_derivatives(x,y,direction):
    unit_direction=direction/np.linalg.norm(direction)
    return np.dot(gradient_T(x,y),unit_direction)
#Given point and direction
point=(-1,3/2)
direction=np.array([-1,-1/2])
#Compute and print results
grad_at_point=gradient_T(*point)
dir_deriv=directional_derivatives(*point,direction)
print(f'Gradient at {point} \u2192  {grad_at_point}')
print(f'Directional Derivative at {point} in direction {direction} \u2192 {dir_deriv}')
#Plot the directional derivatives  over the given region
x_val=np.linspace(-2,0,30)
y_val=np.linspace(0,2,30)
X,Y=np.meshgrid(x_val,y_val)
Z=np.vectorize(lambda x,y:directional_derivatives(x,y,direction))(X,Y)

fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap='coolwarm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Directional derivative value')
ax.set_title('Directional Derivative Over a Surface')
plt.show()