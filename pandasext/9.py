import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('test2.csv')

# df = df.replace(
#     to_replace = {'-'},                     #to_replace = - jadi method
#     method = 'bfill'
# )

#combine replace and method (ffill/bfill)

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

print(df) 

# print(df)