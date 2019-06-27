import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_json('0.json')

cols = df.columns.tolist()
print(cols)
cols=cols[-1:] + cols[:-1]
df=df[cols]
# print(df[df['kota']=='Jakarta'])
# df=df[['id','nama','kota']]
print(df)

df.to_csv('haha.csv', index = False)
#pip3 install openpyxl 
#pip3 install xlwt
df.to_excel('haha.xls', index = False) #hilangin index didepan table
df.to_json('haha.json', orient = 'records') 
#prettify json = cmd + shift + p
#orient = records,values,index,table,columns

