import numpy as np
from matplotlib import pyplot as plt

x = np.arange(5)
y = np.array([1,2,3,4,5])
z = 2 * y

# fig 1
plt.figure('Ini grafik nomor satu', figsize=(10,5))

# plot 1
plt.subplot(1,2,1)              #row,column,position
plt.plot(x,y,'r-')
plt.grid(True)
plt.title('Plot 1')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend(['Hubungan XY'])

# plot 2
plt.subplot(1,2,2)
plt.plot(x,y,'g--')
plt.grid(True)
plt.title('Plot 2')
plt.xlabel('Nilai x')
plt.ylabel('Nilai z')
plt.legend(['Hubungan XZ'])

plt.savefig('3chart.png')
plt.show()