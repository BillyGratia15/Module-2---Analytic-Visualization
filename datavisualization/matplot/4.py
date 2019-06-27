#scatter,bar,histogram,pie chart
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(5)
y = np.array([1,2,3,4,5])
z = 2 * y

#----------------SCATTER CHART-----------------#
# plt.scatter(x,y, color='y', marker='*', s=500)        # scatter diagram
# plt.plot(x,y,'r--')

#----------------BAR CHART-------------------#
# plt.bar(x,y, color='blue', yerr=.4)                   # yerr= margin of error
# plt.bar(x,z, color='yellow', bottom = y )             # pake bottom buat stack/ditumpuk 

#----------------HISTOGRAM---------------------#
# plt.hist([y,z],x, histtype='bar', rwidth=.5)

#----------------PIE CHART----------------------#
warna = 'r','orange','y','g','b'
plt.pie(x,labels=x, startangle=180, colors=warna,       # startangle=startposition
    shadow=True, explode=(0,0,0.1,0,0),                 # explode = narik diagram          
    autopct='%1.1f%%', textprops={'color':'w'}          # autopct = show percent (.1f = 1 decimal)
)
plt.legend(x)

plt.show()