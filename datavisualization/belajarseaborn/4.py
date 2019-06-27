#pip3 install seaborn

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid')

dataku = sn.load_dataset('flights')
print(dataku)

sn.swarmplot(x='year',y='passengers', data=dataku)
plt.xticks(rotation=90)
plt.savefig('4sn.png')
plt.show()