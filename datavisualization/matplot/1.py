import matplotlib.pyplot as plt
import numpy as np

x = np.arange (10)
y = np.array([8, 3, 2, 5, 6, 7, 2, 4, 7, 6])

# plt.plot(x,y,x,y**2,x,y**3)
# plt.plot(x,y,'g--',x,y**2,'b^',x,y**3,'r')
# print(plt.style.available)                               #list of available style 
plt.style.use('seaborn')

plt.plot(x,y,'--',color = 'purple', linewidth=3)           #o = bisa style bisa color

plt.fill_between(x,y[3],y[1], 
facecolor='y', 
alpha=.3)                                           #fillcolor, alhpha = transparant

for titik in x:
    plt.text(titik-.1, y[titik]+.2, y[titik])       #x,y,value

plt.annotate(
    'Nilai tertinggi', xy=(0,8), xytext=(1,7),
    #arrowprops = dict(facecolor='blue', shrink=.2)  #shrink untuk mendekin panah
    arrowprops = dict(arrowstyle='wedge')
)

plt.plot(x,y, 'r*')

plt.text(0,8,'Titik\nMax')
plt.title('Tes Matplotlib')

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.xticks(np.arange(0, 10, step =1))                                #rotate x and ylabel
plt.yticks(rotation = 60)

plt.grid(True)

plt.legend('x-y',loc=0)            #loc ---> legend location

plt.subplots_adjust(                                     #adjust
    left=.14, bottom=.14, right=.95, top=.88,
    wspace=.2, hspace=.2
)

plt.savefig('1chart.png')
plt.show()                                               #untuk show grafiknya