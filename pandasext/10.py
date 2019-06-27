import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('test3.csv')

df = df.replace({
    'nama':['-','+'],
    'job' : 'not available'
},{
    'nama':['Andini','Bambang'],
    'job' : 'jobless'
})

df['usia'] = df['usia'].replace(
    to_replace = ['-', '-1'],
    method = 'bfill'
)

# print(df[df['kota'] == 'Jakarta'])              #show data yang di Jakarta aja

# penulisan pake groupby #
dfkota = df.groupby('kota')
# print(dfkota.get_group('Jakarta'))

# print(dfkota.max())                             #show max per kota tapi per kolom, gak related 
# print(dfkota.min())                             #show min per kota  
# print(dfkota.min(numeric_only='int'))           #show min per kota cuma yang integer
# print(dfkota.min(level='usia'))                 #show min per kota di level usia    

'''''''''''''''''''''''
# df2 = [
#     {'nama':'Mr.X', 'usia':22, 'job':'PNS', 'kota': 'Bogor'},
#     {'nama':'Mr.Z', 'usia':24, 'job':'PNS', 'kota': 'Medan'}
# ]

# df2 = pd.DataFrame(df2)                           #make new dataframe  
# print(df2)

# dfAll = pd.concat([df,df2])                       #combining 2 dataframe, index sesuai dataframe itu sendiri
# dfAll = pd.concat([df,df2], ignore_index = True)  #combining 2 dataframe, index lanjut dari dataframe sebelumnya
# dfAll = pd.concat([df,df2], keys=['DF1','DF2'], sort = False)   #combining dataframe dan dikasih key!
# print(dfAll.loc['DF1'])
# print(dfAll)
'''''''''''''''''''''''

# combining kalo data yang beririsan #

# df2 = [
#     {'nama':'Mr.X', 'usia':22, 'berat':77},
#     {'nama':'Mr.Z', 'usia':24, 'berat':55}
# ]

# df2 = pd.DataFrame(df2) 

# dfAll = pd.concat([df,df2], ignore_index=True, sort = False)
# print(dfAll)

# df2 = [                                             #nambahin data di data yang sudah ada
#     {'nama':'Andini', 'berat':77},
#     {'nama':'Budi', 'berat':55}
# ]

# df2 = pd.DataFrame(df2) 

# dfAll = pd.concat([df,df2], axis=1, ignore_index=True, sort = False)
# print(dfAll)

df2 = [
    {'nama':'Caca', 'berat':54},
    {'nama':'Budi', 'berat':55}
]
df2 = pd.DataFrame(df2, index=[2,1])
dfAll = pd.concat([df,df2], axis=1)

print(dfAll)

