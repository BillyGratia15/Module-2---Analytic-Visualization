from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ganteng12345'
app.config['MYSQL_DB'] = 'tes_flask'


# home route
@app.route('/')
def home():
    return '<h1>Selamat datang!</h1>'

@app.route('/dataku', methods = ['GET', 'POST'])
def dataku():
    if request.method == 'GET':
        x = mysql.connection.cursor()
        jmlData = x.execute('select * from mytable')
        print(jmlData)
        if jmlData > 0:
            data = x.fetchall()
            print(data)

            allData = []
            for i in range(len(data)):
                id = data[i][0]
                nama = data[i][1]
                usia = data[i][2]
                dataDict = {
                    "id" : id,
                    "nama" : nama,
                    "usia" : usia
                }
                allData.append(dataDict)
            return jsonify(allData)
        else:
            return jsonify({'status' : 'Tidak ada data'})
    else:
        nama = request.form['haha']
        usia = request.form['hihi']
        
        x = mysql.connection.cursor()
        x.execute(
            'insert into mytable (nama, usia) values (%s, %s)', 
            (nama, usia)
        )                                                                       
        mysql.connection.commit()              
        return jsonify({'status' : 'Anda nge-POST'})  

# formulir
@app.route('/formulir')
def formulir():
    return render_template('formulir.html')

# activate server
if __name__ == '__main__':
    app.run(debug = True)