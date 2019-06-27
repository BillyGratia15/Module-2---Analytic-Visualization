#DETERMINANT INVERSE TRANSPOSE

import numpy as np

a = np.array ([[1,0,0],[2,6,0],[4,5,2]])

print(round(np.linalg.det(a)))
print(np.linalg.inv(a))
print(np.transpose(a)) #bisa juga print(a.transpose())
