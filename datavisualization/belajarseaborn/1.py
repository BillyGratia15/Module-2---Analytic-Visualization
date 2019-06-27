#pip3 install seaborn

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid')

dataku = sn.load_dataset('flights')                 #ambil data dari github
#dataku = data.pivot('month','year','passengers')   #better display
print(dataku)

sn.lmplot(                                  #regresi linear
    x='year',
    y='passengers',
    data=dataku,
    hue='month',
    )

plt.savefig('1sn.png')
plt.show()