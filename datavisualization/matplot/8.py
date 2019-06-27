#pip3 install pillow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# black/white = 'L' / 'RGBA' / 'CMYK'
gambar = Image.open('1chart.png').convert('L')
gambar = np.array(gambar)

print(gambar)

# plt.imshow(gambar,cmap='gray')
# plt.show()

gbr = Image.fromarray(gambar, 'L')    #pake pillow kebukanya di image viewer
gbr.show()