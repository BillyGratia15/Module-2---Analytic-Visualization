import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''''''
s1 = pd.Series(np.arange(1,6))
df = pd.DataFrame({
    'A' : s1,
    'B' : s1
})

''''''

df = pd.DataFrame({
    'nomor' : [1,2,3,4,5],
    'nama' : ['Andi','Budi','Caca','Deni','Euis'],
    'gender' : pd.Categorical(['L','L','P','L','P']),
    'kota' : ['Makassar','Jakarta','Bandung','Bogor','Palu'],
    'tanggal' : pd.Timestamp('20191228'),                       #yyyymmdd
    'tgl2' : pd.date_range('20191228', periods = 5)         
})


tgl = pd.Timestamp('20201212')
print(tgl)
print(pd.Series(tgl).dtypes)
print(type(tgl))

tgl2 = pd.date_range('20190928', periods = 3) 
print(tgl2)
print(pd.Series(tgl2).dtypes)
print(type(tgl2))


# print(df)