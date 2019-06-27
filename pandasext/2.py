import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pip3 install xlrd
df1 = pd.read_excel('data.xls','Sheet1')
df1.set_index('id')
df1.sort_values(by='id')
df2 = pd.read_excel('data.xls','Sheet2')
df2.set_index('id')
df2.sort_values(by='id')
df1['gaji'] = df2['gaji']
print(df1)
