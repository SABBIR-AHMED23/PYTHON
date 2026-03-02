import numpy as np
from scipy.integrate import dblquad,tplquad
f1=lambda z,y,x: x*np.exp(-y)*np.cos(z)
result1=tplquad(f1,0,1,lambda x:0,lambda x:1-x**2,lambda x,y:3,lambda x,y:4-x**2-y**2)[0]
print(f'The first integral solution: {result1}')

f2=lambda y,x: (x*y)/np.sqrt(x**2+y**2+1)
result2=dblquad(f2,0,1,lambda x:0,lambda x:1)[0]
print(f'The second integral solution: {result2}')