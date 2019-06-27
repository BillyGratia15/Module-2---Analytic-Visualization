import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv 

playersData = pd.read_csv('data.csv')

playersData1=playersData[playersData['Age']>=25][playersData['Overall']>=85]
playersData2=playersData[playersData['Age']>=25][playersData['Overall']<85]
playersData3=playersData[playersData['Age']<25][playersData['Overall']>=85]
playersData4=playersData[playersData['Age']<25][playersData['Overall']<85]


plt.scatter(playersData1['Age'],playersData1['Overall'],color='blue')
plt.scatter(playersData2['Age'],playersData2['Overall'],color='red')
plt.scatter(playersData3['Age'],playersData3['Overall'],color='green')
plt.scatter(playersData4['Age'],playersData4['Overall'],color='yellow')

plt.grid(True)
plt.legend(['Old++','Old--','Young++','Young--'])
plt.xlabel('Age')
plt.ylabel('Performance')

plt.show()

