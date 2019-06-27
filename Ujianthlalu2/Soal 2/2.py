import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# x  - 2y +  z =  6
# 3x +  y - 2z =  4
# 7x - 6y -  z = 10

a = np.array([[1,-2,1],[3,1,-2],[7,-6,-1]])
b = np.array([6,4,10])
c = np.linalg.solve(a,b)

print('Nilai x = ', round(c[0]))
print('Nilai y = ', round(c[1]))
print('Nilai z = ', round(c[2]))

plt.figure('Math')

x1 = np.array([[b[0]/a[0][0], 0, 0]])
y1 = np.array([0, b[0]/a[0][1], 0])
z1 = np.array([[0, 0, b[0]/a[0][2]]])

myplot = plt.subplot(131, projection = '3d')
myplot.plot_wireframe(x1, y1, z1, facecolor = 'red', alpha = 0.3)
myplot.scatter(x1, y1, z1, color = 'blue', s = 20)
myplot.set_title('x - 2y + z = 6')
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')

x2 = np.array([[b[1]/a[1][0], 0, 0]])
y2 = np.array([0, b[1]/a[1][1], 0])
z2 = np.array([[0, 0, b[1]/a[1][2]]])

myplot = plt.subplot(132, projection = '3d')
myplot.plot_wireframe(x2, y2, z2, facecolor = 'darkgreen', alpha = 0.3)
myplot.scatter(x2, y2, z2, color = 'red', s = 20)
myplot.set_title('3x + y - 2z = 4')
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')

x3 = np.array([[b[2]/a[2][0], 0, 0]])
y3 = np.array([0, b[2]/a[2][1], 0])
z3 = np.array([[0, 0, b[2]/a[2][2]]])


myplot = plt.subplot(133, projection = '3d')
myplot.plot_wireframe(x3, y3, z3, facecolor = 'blue', alpha = 0.3)
myplot.scatter(x3, y3, z3, color = 'green', s = 20)
myplot.set_title('7x - 6y - z = 10')
myplot.set_xlabel('Nilai X')
myplot.set_ylabel('Nilai Y')
myplot.set_zlabel('Nilai Z')


plt.show()