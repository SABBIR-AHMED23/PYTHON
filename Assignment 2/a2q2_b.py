import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
s=sp.Symbol('s')
#Function for arc length parameterization
def r(s):
    t=s/np.sqrt(2)
    return np.array([sp.cos(t), sp.sin(t), t])
#Compute final position after walking 10 units
s_final=10
start=r(0)
end=r(s_final)
#Generate helix points
t_val=np.linspace(0,end[2]+2,200)
x_val, y_val, z_val=np.cos(t_val), np.sin(t_val), t_val
#Plot the helix
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection='3d')
ax.plot(x_val,y_val,z_val)
#Mark start & end points
ax.scatter(*start,color='r',s=100,label='Start(1,0,0)')
ax.scatter(*end,color='g',s=100,label='End after s=10')
#Levels & settings
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Bug\'s walking along the helix')
ax.legend()
plt.show()
#Print results
print('The arc length parameterization: ',r(s))
print('Final position after walking 10 units: ',end)