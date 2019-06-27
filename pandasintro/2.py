import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nama = np.arange(10)

nama = pd.Series(
    nama,
    name = 'Students',
    # index = ['a','b','c']
    )

plt.plot(nama,nama)
plt.show()

