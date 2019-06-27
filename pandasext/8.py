import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')

###replace method = replace tidak hanya untuk missing value (not only NaN)

# df = df.replace(['-','-1','not available'],np.NaN)      #replace [] jadi 0, np.Nan, atau string 
# df = df.replace(['-','-1','not available'],NaN)         #NaN nya kebaca string, jadi gabisa di ubah pake fillna  
# df = df.fillna('haha')                                  #ngubah si NaN                                                  

df = df.replace({
    '-':'+',
    '-1':'+1',
    'not available':'available'
})


print(df)