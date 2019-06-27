#pip3 install seaborn

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid')

dataku = sn.load_dataset('flights')                 #ambil data dari github
#dataku = data.pivot('month','year','passengers')   #better display
print(dataku)

sn.relplot(
    x='year',
    y='passengers',
    data=dataku,
    # kind='line'
    hue='month',
    size='month'
    #style='month'
    )

plt.savefig('0sn.png')
plt.show()