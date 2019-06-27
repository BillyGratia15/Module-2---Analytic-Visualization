from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Selamat datang!</h1>'

@app.route('/data')
def data():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'Ganteng12345',
        database = 'tes_flask'
    )

    x = mydb.cursor()
    x.execute('select * from mytable')
    data = x.fetchall()

    print(data)

    hasilData = []
    for i in range(len(data)):
        id = data[i][0]
        nama = data[i][1]
        usia = data[i][2]
        hasil = {
            'id' : id,
            'nama' : nama,
            'usia' : usia
        }
        hasilData.append(hasil)
    return jsonify(hasilData)


if __name__ == '__main__':
    app.run(debug = True)

