#BACA DATA CSV without numpy

import matplotlib.pyplot as plt
import csv


x = []
y = []
with open('data.csv','r') as dataku:
    data = csv.reader(dataku)
    for i in data:
        x.append(int(i[0]))
        y.append(int(i[1]))

print(x)
print(y)
plt.plot(x,y)
plt.savefig('6chart.png')
plt.show()

