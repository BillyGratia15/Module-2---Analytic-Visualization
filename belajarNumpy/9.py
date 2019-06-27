import numpy as np

# print(np.exp(2))                     # e ^ 2 = 7.38905609893065 
# print(np.log(7.38905609893065))      # e log 7,39  = ln 7.39 = 2
# print(np.log10(1000))                # 10 log 1000 = 3

# a = np.random.randint(5, size=(1,5))
# print(a)
# print(np.mean(a))
# print(np.median(a)) #diurutin dulu terus nyari angka tengah

b = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.mean(b))
print(np.mean(b, axis=0)) #rata2 perkolom
print(np.mean(b, axis=1)) #rata2 per
