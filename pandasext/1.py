import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# print(df.head())
# print(df.column())

# #showing the highest overall skill
# print(df['Overalll'].max())
# print(df['Overalll'].min())
# print(df['Overalll'].mean())

# print(df['Age'].max())

# #showing player who has the specific criteria:
# print(df(df['Overall'] == df['Overall'].max()])
# print(df(df['Overall'] == df['Overall'].max()]['Name'])
# print(df(df['Overall'] == df['Overall'].max()][['Name','Club']])

# #showing players who have the overall skill above 90
# print(df[df['Overall'] >= 90]['Name'])
# print(df[df['Overall'] >= 90][['Name','Position','Club']])
# print(df[['Name','Position','Club']][df['Overall'] >= 90])


# # real madrids player
# print(
#     df[['Name','Position','Club']]
#     [df['Overall'] >= 90]
#     [df['Club'] == 'Real Madrid'] 
# )

df = df[['Name','Position','Club','Overall']][df['Overall'] >= 90]
df = df[df['Club'] == 'Real Madrid']
# print(df)
# print(df.iat[1,3])          #specific index
# print(type(df['Overall']))

print(df.T)                     #transpose column and row
print(df.T.index)
