# LATIHAN MATRIKS
import numpy as np

# 3x + y = 9
# x + 2y = 8

a = np.array([[3,1],[1,2]])
b = np.array([9,8])
c = np.linalg.solve(a,b)
print(c)

#  x +  y - z = -3
#  x + 2y + z = 7
# 2x +  y + z = 4

d = np.array([[1,1,2],[1,2,1],[-1,1,1]])
e = np.array([-3,7,4])
f = np.linalg.solve(d,e)
print(f)

# 3x = 9
g = np.array([[3]])
h = np.array([9])
i = np.linalg.solve(g,h)
print(i)

