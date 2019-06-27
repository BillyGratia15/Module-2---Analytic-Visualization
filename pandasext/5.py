import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    'tlkm.csv',
    index_col=False,                #index_col = False (agar kolomnya sesuai)
    parse_dates=['Tanggal']         #ngubah type string tanggal jadi timestamp
)

# print(df.head())
# print(type(df['Tanggal'][0]))

df = df.set_index('Tanggal')
df = df.sort_index()                        #ubah datanya jadi ascending

# print(df['2019-02'])                      #tampilin data di bulan feb. tanggal harus jadiin timestamp dulu
# print(df.loc['2019-02-27'])
# print(df['2019-02-27':'2019-02-27']) 
# print(df['2019-02-27':'2019-02-28'])

# print(df['2019-03']['Close'])             #show all 'close' (march)
# print(df['2019-03']['Close'].mean())      #average 'close'
# print(df['2019-03']['Close'].max())       #max 'close'
# print(df['2019-03']['Close'].min())       #min 'close'

# print(df[df['Close'] == df['2019-03']['Close'].max()])      #cari 'close' terbesar di tanggal berapa

plt.plot(
    df.index, df['Close'],'g-',
    df.index, df['Open'],'r-'
)

plt.xlabel('Tanggal')
plt.xticks(rotation=65)
plt.ylabel('Rp')
plt.grid(True)

plt.show()