#BACA DATA CSV with numpy

import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt(
    'data.csv',
    delimiter = ',',
    unpack = True
)

print(x)
print(y)
plt.plot(x,y)
plt.savefig('5chart.png')
plt.show()