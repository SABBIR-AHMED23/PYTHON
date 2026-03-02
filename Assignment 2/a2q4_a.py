import numpy as np
import matplotlib.pyplot as plt
levels=[1,4,9,16,26,36] # Define contour levels
x=np.linspace(-3,3,100)
y=np.linspace(-3,3,100)
X,Y=np.meshgrid(x,y)
F1=4*X**2+Y**2
plt.contour(X,Y,F1,levels,cmap='jet')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour of f(x,y)=$4x^2+y^2$')
plt.show()

Z=np.sqrt(X**2+Y**2 +np.array(levels)[:,None,None])
for i in range(len(levels)):
    plt.contour(X,Y,Z[i],levels=1,cmap='coolwarm')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour of f(x,y,z)=$z^2-x^2-y^2$')
plt.show()