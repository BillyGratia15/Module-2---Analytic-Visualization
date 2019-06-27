import matplotlib.pyplot as plt
import matplotlib.image as mimg

gambar = mimg.imread('4pie.png')
gambar = gambar[:,:,1]

'''''
print(gambar)
print(gambar.ndim)
print(gambar.shape)
print(len(gambar[0]))
'''''

gbrplot = plt.imshow(gambar, cmap='BuPu')
plt.show()