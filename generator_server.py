import json
import os
import numpy as np
from static.Detect.get_number_file import (
    get_number_file
)
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
# from model.MelLearning import(
#     transFormat,
#     getMelPic
# )
# from model.tuneAnalyse.call_predictor import(
#     predictor
# )
# from model.lyricAnalyse.get_result import(
#     result
# )
# 先要初始化一个 Flask 实例
# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")

app = Flask(__name__, static_folder='views/statics')
app = Flask(__name__, static_url_path='')


@app.route('/show.bg', methods=['GET'])
def showBG():
    path = './static/image/background/'
    number = str(get_number_file(path))
    # print("number:",number)
    return number


@app.route('/show.fig', methods=['GET'])
def showFig():
    path = './static/image/figure/'
    number = str(get_number_file(path))
    print("number:",number)
    return number


# 运行服务器
if __name__ == '__main__':
        # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
        # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=False,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
    # app.run() 开始运行服务器
    # 所以你访问下面的网址就可以打开网站了
    # http://127.0.0.1:2000/
    # lyricResult()
