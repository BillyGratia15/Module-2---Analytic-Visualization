import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
z1 = np.array([0,0,0,0,0])                          #z1 = np.zeros(5)

x1 = np.array([1,1,1,1,1])                          #x1 = np.ones(5)   
y1 = np.array([1,1,1,1,1])                          #y1 = np.ones(5)
z = np.array([1,3,5,7,9])

plt.figure('Tes 3D Bar')
myplot = plt.subplot(111, projection = '3d')
myplot.bar3d(x,y,z1,x1,y1,z,
    color =['black','pink','black','pink','black'])  #color per bar

myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')
myplot.set_title(label='Tes 3D Bar', loc='left')

plt.savefig('3d1.png')
plt.show()



