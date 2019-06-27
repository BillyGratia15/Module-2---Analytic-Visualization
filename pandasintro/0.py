import pandas as pd

nama = ['Andi','Budi','Caca'] #harus list
nama = pd.Series(
    nama,
    name = 'Students',
    # index = ['a','b','c']
    )

print(nama)
print(nama[0])
print(nama[0:3:2])

