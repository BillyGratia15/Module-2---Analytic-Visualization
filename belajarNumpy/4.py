import numpy as np

a = [
    (1,2,3,4,5),
    (4,5,6,7,8)
]

a = np.array(a)
print(a[1,4])       
print(a[0,4])
print(a[0:,0:])         #print semua index
print(a[0:,3:])         #print seluruhnya tapi mulai dari index ke 3 tiap elemen
print(a[0:,3])          #print tiap elemennya cuma index ke 3
print(a[0:, [0,-1]])    #print tiap elemennya index 0 dan index -1
