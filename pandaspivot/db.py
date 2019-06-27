#pip3 install mysql-connector-python
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ganteng12345',
    database = 'fauna'
)

query = 'select * from aves'
df = pd.read_sql(query, con = mydb)
print(df)