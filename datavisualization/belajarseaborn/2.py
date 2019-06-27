#pip3 install seaborn

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid')

dataku = sn.load_dataset('flights')                 #ambil data dari github
#dataku = data.pivot('month','year','passengers')   #better display
print(dataku)

sn.catplot(
    x='year',
    y='passengers',
    data=dataku,
    hue='month',                        #diff color
    kind= 'bar',
    )

plt.savefig('2sn.png')
plt.show()