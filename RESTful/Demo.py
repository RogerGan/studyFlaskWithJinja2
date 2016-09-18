# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2016-09-18 16:34'

__mail__ = 'chaojiang.gcj@alibaba-inc.com/393037282@qq.com'

__weibo__ = 'http://weibo.com/ganchaojiang'


from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)