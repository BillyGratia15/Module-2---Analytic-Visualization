import numpy as np

# numpy array from list
x1 = [1,2,3,4,5,6]
x2 = (1,2,3,4,5,6)
x3 = {1,2,3,4,5,6}
y = np.array(x3)

print(y)
print(type(y))

# numpy array = np.arange
z = np.arange(50,100,2) # np.arange (start, stopbefore, step)
print(z)
print(z[0])             # index ke 0
print(z[5::2])          # index ke 5 dengan step 2
print(z.ndim)           # dimension
print(len(z))           # jumlah    
print(z.size)           # sama kayak len
print(z.itemsize)       # bytes B
print(z.dtype)          

z2 = np.array([1, 'a', 2, 'b', 3, 'c'])

print(z2)
print(z2.ndim)           
print(len(z2))               
print(z2.size)           
print(z2.itemsize)       
print(z2.dtype)   


