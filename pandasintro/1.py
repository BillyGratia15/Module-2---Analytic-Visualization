import pandas as pd
import numpy as np

nama = np.array([11,12,13,14,15])           #np.array bisa dipake untuk pandas
# nama = np.array(['Andi','Budi','Caca'])   #np.array string bisa juga

nama = pd.Series(
    nama,
    name = 'Students'
    )

print(nama)
print(nama[0])
print(nama[0:3:2])

