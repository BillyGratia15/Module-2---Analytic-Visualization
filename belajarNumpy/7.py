# DOT PRODUCT
import numpy as np

a = np.array([
    [2,1,4,3],
    [2,5,1,2],
    [1,3,2,2]
])
b = np.array([[1,3],[3,2],[2,5],[1,4]])
print(a.dot(b))
print(np.dot(a,b))  #same
print(a@b)          #same
