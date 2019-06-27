import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# #dataframe list of list# #
# data=[
#     ['Andi',90],
#     ['Budi',80],
#     ['Caca',95],
#     ['Deni',65],
#     ['Euis',70],
# ]


# #dataframe list of tuple# #
# data=[
#     ('Andi',90),
#     ('Budi',80),
#     ('Caca',95),
#     ('Deni',65),
#     ('Euis',70),
# ]
# dfData = pd.DataFrame(data,columns=['name','score'])
# print(dfData)
# baris, kolom = dfData.shape
# print(baris)
# print(kolom)

# #dataframe numpy array# #
# data = np.arange(10)
# dfData = pd.DataFrame(data,columns=['score'])
# print(dfData)
# baris, kolom = dfData.shape
# print(baris)
# print(kolom)



#dataframe dictionary# #
data = {'nama': pd.Series(['Andi','Budi','Caca']),
       'score' : pd.Series([87,78,90])} 
dfData = pd.DataFrame(data)      
print(dfData)
baris, kolom = dfData.shape
print(baris)
print(kolom)



