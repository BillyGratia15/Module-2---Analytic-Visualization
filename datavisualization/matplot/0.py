# pip3 install matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.arange (10)
y = np.array([8, 3, 2, 5, 6, 7, 2, 4, 7, 6])

# plt.plot(x,y,x,y**2,x,y**3)
# plt.plot(x,y,'g--',x,y**2,'b^',x,y**3,'r')
# print(plt.style.available)                               #list of available style 
plt.style.use('dark_background')

plt.plot(x,y,'-o',color = 'purple', linewidth=3)           #o = bisa style bisa color
plt.plot(x,y**2,'g--')                                   #g-- = green--
plt.plot(x,y**3,'b*-')                                   #b=blue *


plt.title('Tes Matplotlib')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.xticks(rotation = 90)                                #rotate x and ylabel
plt.yticks(rotation = 60)

plt.grid(True)

plt.legend(['x-y', 'x-y**2', 'x-y**3'],loc=0)            #loc ---> legend location

plt.savefig('0chart.png')
plt.show()                                               #untuk show grafiknya