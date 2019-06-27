import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dataframe
nilai = [2,3,4,6,2,4,7,9,1]
nama = ['a','b','c','d','e','f','g','h','i']

# dfNilai= pd.DataFrame(nilai, columns=['Nilai'])     #give column name from 1 list
dfNilai= pd.DataFrame()
dfNilai['score'] = nilai                        #column name = score
dfNilai['name'] = nama                          #column name = nama

print(dfNilai) 