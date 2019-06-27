import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv('0.csv',skiprows=2)

df = pd.read_csv(
    '0.csv',
    header=None,
    names = ['no KTP','nama lengkap', 'score']
)

print(df)