import mysql.connector 
from flask import Flask, jsonify,  request , render_template

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Ganteng12345',
    database='tes_flask'
)

app=Flask (__name__)

#home route
@app.route('/')
def home():
    return '<h1>selamat datang!</h1>'

#route GET and POST data
@app.route('/dataku',methods=['GET','POST'])
def dataku():
    x=mydb.cursor()
    x.execute('select * from mytable')
    data=x.fetchall()
    print(data)
    jml=len(data)
    
    if request.method=='GET':
        if jml > 0:
            
            allData=[]
            for i in range(len(data)):
                id=data[i][0]
                nama=data[i][1]
                usia=data[i][2]
                dataDict={
                    "id":id,
                    "nama":nama,
                    "usia":usia
                }
                allData.append(dataDict)
            return jsonify(allData)   
        else:
            return jsonify({'status':'tidak ada data'})
        print(allData) 
    else :
        # body=request.json
        # nama=body['nama']
        # usia=body['usia']
        nama=request.form['haha']
        usia=request.form['hihi']

        x=mydb.cursor()
        x.execute('insert into mytable (nama, usia) values (%s, %s)',(nama,usia))
        mydb.commit()
        return jsonify ({'status':'anda nge-POST'})

#formulir
@app.route('/formulir')
def formulir():
    return render_template('formulir.html')
    
#activate server
if __name__=='__main__':
    app.run (debug=True)