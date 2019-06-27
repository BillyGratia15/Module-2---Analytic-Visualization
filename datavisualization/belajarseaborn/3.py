#pip3 install seaborn

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid')

dataku = sn.load_dataset('flights')                 #ambil data dari github
dataku = dataku.pivot('month','year','passengers')   #better display
print(dataku)

sn.heatmap(dataku, cmap='BuPu_r', annot=True, fmt='d')  #annot=display angka, fmt = digit
plt.savefig('3sn.png')
plt.show()