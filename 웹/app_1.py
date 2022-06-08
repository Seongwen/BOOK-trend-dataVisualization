from datetime import date
import re
from flask import Flask, render_template ,request ,redirect, url_for
import os

import pymysql

app = Flask(__name__) #플라스크 객체생성

@app.route('/') #'/'를 호출하면 아래의 함수를 실행
def index():
    return render_template('index.html')
##################################

#
@app.route('/index2') 
def index2():
    return render_template('index2.html')

@app.route('/team') 
def team():
    return render_template('team.html')

@app.route('/main') 
def mainp():
    return render_template('main.html')

@app.route('/thx') 
def thx():
    return render_template('thx.html')

##################################
if __name__ == '__main__':
     # 동작
    app.run(debug = True)
    # app.run()
    # app.debug = True
