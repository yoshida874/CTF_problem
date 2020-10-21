# -*- coding: UTF-8 -*-
from flask import Flask,request,render_template,make_response,escape
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    name = 'HOGE'
    cookie_name = ''

    if request.method == 'POST':

        cookie_name = escape(request.form['name'])
        name = escape(request.form['name'])

        if name == 'admin':
            name = 'not admin'

        flag = get_flag(name)
        response = make_response(render_template("hello.html", title='星', name=name, flag=flag)) 
        max_age = 10
        expires = int(datetime.now().timestamp()) + max_age
        response.set_cookie('name', value=cookie_name, max_age=max_age, expires=expires, path='/', secure=None, httponly=False)
        
    else:
        name = request.cookies.get('name', None)
        flag = get_flag(name)
        response = make_response(render_template("hello.html", title='星', name=name, flag=flag)) 

    return response


def get_flag(name):
    if name == 'admin':
        flag = 'wizCTF{Variable_direct_cookie}'
    else:
        flag = 'adminだけがFlagを見ることができます'

    return flag


## おまじない
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))