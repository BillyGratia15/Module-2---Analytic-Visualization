from flask import Flask, render_template, request, send_from_directory
import matplotlib.pyplot as plt
import requests
import numpy as np

app=Flask(__name__)
app.config['upload_folder']='./'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/grafik', methods=['POST','GET'])
def grafik():
    if request.method=='POST':
        x=list(request.form['x'].replace(',',''))
        y=list(request.form['y'].replace(',',''))
        x=np.array(x).astype(int)
        y=np.array(y).astype(int)
        print(x)
        print(y)
        plt.figure('Data anda')
        plt.plot(x,y)
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')
        plt.xticks(np.arange(-2,max(x)))
        plt.yticks(np.arange(-2,max(y)))
        plt.grid(True)
        plt.savefig('grafik.png') 
        return render_template('grafik.html')

@app.route('/load/<path:x>')
def load(x):
    return send_from_directory('./',x)    


if __name__=='__main__':
    app.run(debug=True)