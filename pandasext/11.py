#df.merge FUNCTION
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

df2 = [
    {'nama':'Caca', 'berat':54},
    {'nama':'Budi', 'berat':55}
]
df2 = pd.DataFrame(df2)
# dfAll = pd.merge(df,df2, on='nama')                 
dfAll = pd.merge(df,df2, on='nama',how='left')


print(dfAll)