
from pymongo import MongoClient

x = MongoClient('mongodb://localhost:27017/')

#print(x.list_database_names()) #munculin database dari mongo

db = x['tesflask']
col = db['produk']
cari = {'harga':{'$gt': 1000000}}
cari2 = {'nama': 'Headset'}

#print(list(col.find())) #kurang pretty ini ke kanan diprintnya.

# for x in col.find():                #looping jadi PRETTY!
#     print(x)

# for x in col.find(cari):                
#    print(x)
   
# for x in col.find(cari2):                
#    print(x)

nama = input('Ketik nama produk : ')
harga = input('Ketik harga produk : ')

data = {'nama': nama, 'harga': int(harga)}

# data = {'nama': 'Kemoceng', 'harga': 50000}
z = col.insert_one(data)             #untuk masukin data baru ke database mongo
print(z.inserted_id)

for i in col.find({'_id': z.inserted_id}):
    print('Data sukses tersimpan!')
    print(i)

