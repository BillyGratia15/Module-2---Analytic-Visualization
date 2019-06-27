import numpy as np

z = np.random.rand(10)   # 10 angka random range 0-1
print(z)
print(z.ndim, 'dimensi')

z2 = np.random.rand(1,10) #2 dimensi , 1 elemen ada 10 data 
print(z2)
print(z2.ndim, 'dimensi')

z3 = np.random.rand(2,4) #2 dimensi , 2 elemen tiap elemen ada 4 data

print(z3)
print(z3.ndim)           

z4 = np.random.randint(10) # 1 random angka dibawah 10
print(z4)

z5 = np.random.randint(10, size=10) # 1 elemen 10 data random random angka dibawah 10
print(z5)
print(z5.ndim)

z6 = np.random.randint(10, size=(2,5)) # 2 dimensi, 2 elemen masing2 5 data
print(z6)
print(z6.ndim)

z7 = np.random.randint(10, size=(1,10)) # 2 dimensi, 1 elemen ada 10 data
print(z7)
print(z7.ndim)




