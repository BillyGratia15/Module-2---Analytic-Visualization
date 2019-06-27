import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

x = np.ones(5)
y = np.array([2,4,6,8,10])
z1 = np.array([20,20,20,20,20])                          

x1 = np.ones(5)                       
y1 = np.array(([2,2,2,2,2]))                          
z = np.array([1,3,5,7,9])

plt.figure('Tes 3D Bar')
myplot = plt.subplot(111, projection = '3d')
myplot.bar3d(x,y,z1,x1,y1,z,
    color =['black','pink','black','pink','black']) 

myplot.set_xticks([1,2,3,4,5])              #get locations
myplot.set_xlim3d(right=5)                  #distribusi 3dgraph(x,y,z) nya ke kanan

myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')
myplot.set_title(label='Tes 3D Bar', loc='center')

plt.savefig('3d2.png')
plt.show()



