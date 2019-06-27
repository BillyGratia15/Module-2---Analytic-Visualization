import numpy as np

satu = np.array([1,2,3])
dua = np.array([[1,2,3]])
tiga = np.array([[[1,2,3]]])


print(satu)
print(satu.ndim)
print(dua)
print(dua.ndim)
print(tiga)
print(tiga.ndim)

# jumlah dalam list harus sama
a = [
    [1,2,3,4,5],[4,5,6,7,8]
]
a = np.array(a)
print(a)
print(a.shape) # dalam dimensi ada berapa data ---> gampangnya si vertikal,horizontal

b = a.reshape(5,2) 
print(b)
print(b.shape)

c = a.reshape(10,1)
print(c)
print(c.shape)
