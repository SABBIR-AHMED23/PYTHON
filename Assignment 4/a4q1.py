import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(0,10,400)
x2=np.linspace(0,10,400)
X1,X2=np.meshgrid(x1,x2)

constraint1= X1+2*X2<=10
constraint2= X1+X2<=6
constraint3= X1-X2<=2
constraint4= X1-2*X2<=1
non_negativity= (X1>=0) & (X2>=0)

feasible_region= constraint1 & constraint2 & constraint3 & constraint4 & non_negativity
Z= 2*X1+X2
Z_feasible= np.where(feasible_region, Z, -np.inf)

max_value=np.max(Z_feasible)
max_index=np.unravel_index(np.argmax(Z_feasible), Z_feasible.shape)
max_x1=X1[max_index]
max_x2=X2[max_index]

print('Optimal Solution:')
print(f'x1={max_x1:.1f}')
print(f'x2={max_x2:.1f}')
print(f'Maximum Z={max_value:.1f}')

plt.figure(figsize=(8,5))
plt.contourf(X1,X2,feasible_region,levels=[0.5,1],colors='blue')
plt.plot(x1, (10-x1)/2, label=r'$x_1 + 2x_2 \leq 10 $')
plt.plot(x1, 6-x1, label=r'$x_1 + x_2 \leq 6 $')
plt.plot(x1, x1-2, label=r'$x_1 - x_2 \leq 2 $')
plt.plot(x1, (x1-1)/2, label=r'$x_1 - 2x_2 \leq 1 $')
plt.plot(max_x1, max_x2, 'ro', label=f'Max value is {max_value:.1f}')

plt.xlim(0,10)
plt.ylim(0,10)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()