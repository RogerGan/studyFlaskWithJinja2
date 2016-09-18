# -*- coding:UTF-8 -*-
from flask import Flask
from flask import render_template
from flask import request #获取request的公用信息，如User－Agent
from flask import make_response #获取response的信息，例如cookie
from flask import redirect #获取重定向新情况
from flask import abort #处理状态码

app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    # return '<p>Your Browser is %s</p>' % user_agent
    # return '<h1>Bad Requset</h1>', 400
    response = make_response('<h1>This Document carries a cookie!<h1>')
    response.set_cookie('answer', '42')
    # return response
    # return redirect('http://www.example.com')
    return 'Hello World!'

@app.route('/user/<id>')
def get_user(id):
    if id is not '1':
        abort(404)
    return 'hello , %s' % id



@app.route('/install/')
def install():
    return 'install'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':

    app.debug = True
    app.run()
