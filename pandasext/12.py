import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    'tlkm.csv',
    index_col=False,
    parse_dates = ['Tanggal'] )

df = df.head()                          #5 data pertama kalau kurungnya kosong
df = df[['Tanggal','Open','Close']]     #5 data pertama + cuma tanggal open close
print(df)  

print(type(df['Tanggal'][0]))