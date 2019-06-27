import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
z = np.array([[1,3,5,7,9]])  

plt.figure('Tes 3D')
myplot = plt.subplot(111, projection = '3d')
# myplot.plot_wireframe(x,y,z)
# myplot.scatter(x,y,z)
# myplot.plot_wireframe(x,y,z,color='green',linestyle='--')
myplot.scatter(x,y,z,color='y',marker='*',s=200)
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')

plt.savefig('3d0.png')
plt.show()
