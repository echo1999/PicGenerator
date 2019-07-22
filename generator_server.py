import json
import os
import numpy as np
import shutil
from static.Detect.get_number_file import (
    get_number_file
)
from static.Detect.upload import(
    upload_picture
)
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from static.Detect.mix2 import(
    mix_picture
)
from static.Detect.mix2_butterfly import(
    mix_picture_of_butterfly
)
from static.Detect.cut import(
    cut_picture
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


@app.route('/upload.bg', methods=['GET'])
def uploadBG():
    selectNum = request.args['selectNum']
    src = './static/image/background/background'+selectNum+'.jpg'
    dst = './static/image/temp/'
    filename = 'background.jpg'
    upload_picture(src, dst, filename)
    return "ok"


@app.route('/show.fig', methods=['GET'])
def showFig():
    path = './static/image/figure/'
    number = str(get_number_file(path))
    print("number:", number)
    return number


@app.route('/upload.fig', methods=['GET'])
def uploadFig():
    selectNum = request.args['selectNum']
    src = './static/image/figure/figure'+selectNum+'.jpg'
    dst = './static/image/temp/'
    filename = 'figure.jpg'
    upload_picture(src, dst, filename)
    return "ok"


@app.route('/show.bf', methods=['GET'])
def showBF():
    path = './static/image/white_butterfly/'
    number = str(get_number_file(path))
    print("number:", number)
    return number


@app.route('/upload.bf', methods=['GET'])
def uploadBf():
    selectNum = request.args['selectNum']
    src = './static/image/black_butterfly/butterfly'+selectNum+'.jpg'
    dst = './static/image/temp/'
    filename = 'butterfly.jpg'
    upload_picture(src, dst, filename)
    return "ok"


@app.route('/show.reStart', methods=['GET'])
def reStart():
    # 删除抠人像文件夹
    cut_path = './static/image/cut'
    shutil.rmtree(cut_path)  # 能删除该文件夹和文件夹下所有文件
    os.mkdir(cut_path)
    # 删除用户选中图片文件夹
    temp_path = './static/image/temp'
    shutil.rmtree(temp_path)  # 能删除该文件夹和文件夹下所有文件
    os.mkdir(temp_path)
    # 删除融合结果图
    res_path = './static/image/resultPic'
    shutil.rmtree(res_path)  # 能删除该文件夹和文件夹下所有文件
    os.mkdir(res_path)
    return "ok"


@app.route('/show.result', methods=['GET'])
def showResult():
    path = './static/image/temp/'
    fileNum = get_number_file(path)
    # print("fileNum:", fileNum)
    if fileNum == 2:
        background = './static/image/temp/background.jpg'
        figure = './static/image/temp/figure.jpg'
        cut_picture(figure)
        figure_res = './static/image/cut/figure_res.jpg'
        mix_picture(background, figure_res)
    else:
        background = './static/image/temp/background.jpg'
        figure = './static/image/temp/figure.jpg'
        cut_picture(figure)
        figure_res = './static/image/cut/figure_res.jpg'
        mix_picture(background, figure_res)
        background2 = './static/image/resultPic/mixPic1.jpg'
        butterfly = './static/image/temp/butterfly.jpg'
        mix_picture_of_butterfly(background2, butterfly)
    path = './static/image/resultPic/'
    fileNum = get_number_file(path)
    if fileNum == 1:
        return "noBf"
    else :
        return "hasBf"


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
