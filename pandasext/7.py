import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# df = pd.read_csv('test.csv')
# df = pd.read_csv ('test.csv', na_values = ['-','not available']) # '-' dan 'not available' diubah jadi NaN

df = pd.read_csv('test.csv', na_values={              #ubah per column (better ubah semuanya jadi Nan)
    'nama':'-',
    'usia':['-','not available',-1],
    'job':['-','not available']
    }
)                                              

# df = df.fillna(0)                                   #ubah NaN jadi data yang ada di dalam kurung()

# df = df.fillna({                                    #per column  
#     'nama' : 'Anonim',
#     'usia' : 20,
#     'job' : 'Staff'
# })


# df = df.fillna(method='ffill',axis=1)          #yang - not avail ambil data dari index sebelumnya di kolom yang sama.
# df = df.fillna(method='bfill',axis=1)          #yang - not avail ambil data dari index setelahnya di kolom yang sama.    

# df = df.interpolate().fillna({                 #ambil data rata2 dari atas bawah (kira2)
#     'nama':'Anonim',
#     'usia': 20,
#     'job':'Jobless'
# })

# df = df.dropna()                               #kalo ada Nan dibuang datanya
# df = df.dropna(how='all')                      #yang index nya semua datanya kosong akan dibuang
# df = df.dropna(thresh=1)                       #yang ditampilkan hanya data yang minimal 1 kolom terisi
df = df.dropna(subset=['job'])                   #kalau kolom job ada NaN nya, dibuang
print(df)