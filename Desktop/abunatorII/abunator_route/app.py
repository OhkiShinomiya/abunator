# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template,redirect
app = Flask(__name__)
import random
import sys
sys.path.append("/abunator_route/")
import last
name = ''
global key

@app.route('/',methods = ['GET'] )
def index():
    key = str(random.randrange(10**9,10**10)) + 'true'   
    return render_template('/index.html/',\
    key = key,\
    name = '前回の検索結果はありません')

@app.route('/return/<key>',methods = ['GET'])
def returner(key):
    name = last.lastName(key)
    linker = key
    if 'true' in key and name != '':
        return render_template('/index.html',\
        key = linker,\
        name = name)
    elif 'true' in key:
        return render_template('/index.html/',\
        key = linker,\
        name = '前回の検索結果はありません')
    
@app.route('/refer/<key>',methods = ['GET'])
def refer(key):
    linker = key
    name = last.lastName(key)
    if 'true' in key and name != '':
        return redirect('https://abunatorzukan.azurewebsites.net/refer/' + linker + name)
    elif 'true' in key:
        return render_template('/index.html/',\
        key = linker,\
        name = '前回の検索結果はありません' ) 

@app.route('/main/<key>',methods = ['GET'])
def main(key):
    linker = key
    return redirect('https://abunatormain.azurewebsites.net/start/' + linker)

@app.route('/zukan/<key>',methods = ['GET'])
def zukan(key):
    linker = key    
    return redirect('https://abunatorzukan.azurewebsites.net/pic_book/' + linker)


if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)