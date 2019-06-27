import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dataframe list of dictionary#
data = [
    {'nama':'Andi','nilai':90},
    {'nama':'Budi','nilai':88},
    {'nama':'Caca','nilai':89},
    {'nama':'Deni','nilai':89},
    {'nama':'Euis','nilai':89},
]

# dfData = pd.DataFrame(data)
dfData = pd.DataFrame(
    data,
    index = list('abcde')
    )

# print(dfData.head(3))               #show first 3 rows
# print(dfData.tail(2))               #show last 2 rows
# print(dfData.columns)               #tau column nya apa aja, and dtype
# print(dfData.index)                 #indexnya dan rangenya

# print(dfData.values)                #values of data           
# print(type(dfData.values))          #type = np.array  
# print(dfData.describe())            #describe count mean std dll

# print(dfData.sort_index(ascending=False))   #sort descending (defaultnya ascending)
# print(dfData.sort_values(by='nilai',ascending=False))       #sort descending by nilai

# print(dfData.sort_values(
#     by=['nilai','nama'],
#     ascending=[False,False])
#     )                                         #sort descending nama dan nilai

# print(dfData['nama'])
# print(dfData['nilai'])
# print(dfData[0:3])
# print(dfData[0:5:2])

# print(dfData.loc['a'])                          #nama index
# print(dfData.loc['a':'d'])                      #print a sampai d
# print(dfData.loc['a':'d',['nilai']])            #print a sampai d tapi nilai doang
# print(dfData.iloc[0:5:2])                       #urutan index location                             
# print(dfData.iloc[0:5:2, 0:2])                  #baris,kolom

# print(dfData.at['a','nama'])                      #value panggil dg nama index & nama kolom  
# print(dfData.iat[0,1])                            #value panggil dg urutan index & urutan kolom

# print(dfData
#     .iloc[0:5:2]
#     .sort_values(
#         by=['nilai','nama'],
#         ascending = [True, False]                   #nilai ascending nama descending
#     )[['nilai','nama']]                             #nilai dulu baru nama
# )


plt.plot(dfData['nama'], dfData['nilai'])
plt.show()