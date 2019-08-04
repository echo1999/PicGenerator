import json
import os
import numpy as np
import shutil
from PIL import Image, ImageFilter
import cv2
import urllib.request
from static.Detect.compare_fill import(
    Contrast_and_Brightness
)
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
from static.Detect.filter import(
    beauty_face2

)
import datetime
app = Flask(__name__, static_folder='views/statics')
app = Flask(__name__, static_url_path='')


@app.route('/show.bg', methods=['GET'])
def showBG():
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
    path = './static/image/background/'
    number = str(get_number_file(path))
    print("number:", number)
    return number


@app.route('/upload.bg', methods=['GET'])
def uploadBG():
    if os.path.exists('./static/image/temp/background.jpg'):
        return "exist"
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


@app.route('/upload.fig1', methods=['GET'])
def uploadFig1():
    if os.path.exists('./static/image/temp/figure.jpg'):
        return "exist"
    selectNum = request.args['selectNum']
    print("figrue_upload is none 外", selectNum)
    if selectNum == "0":
        print("figrue_upload is none", selectNum)
        src = './static/image/figure2/figure_upload.jpg'
        dst = './static/image/temp/'
        filename = 'figure.jpg'
        upload_picture(src, dst, filename)
        return "ok"
    src = './static/image/figure/figure'+selectNum+'.jpg'
    dst = './static/image/temp/'
    filename = 'figure.jpg'
    upload_picture(src, dst, filename)
    return "ok"


@app.route('/upload.fig2', methods=['GET'])
def uploadFig2():
    if os.path.exists('./static/image/temp/figure.jpg'):
        return "exist"
    picSrc = request.args['picSrc']
    print("picSrc", picSrc)
    rsp = urllib.request.urlopen(picSrc)
    img = rsp.read()
    with open('./static/image/temp/figure.jpg', 'wb') as f:
        f.write(img)
    while True:
        print("等待")
        if os.path.exists('./static/image/temp/figure.jpg'):
            print("图片已经下载成功，返回图片！")
            return "ok"
        continue


@app.route('/upload.bg2', methods=['GET'])
def uploadBg2():
    if os.path.exists('./static/image/temp/background.jpg'):
        return "exist"
    picSrc = request.args['picSrc']
    print("picSrc", picSrc)
    rsp = urllib.request.urlopen(picSrc)
    img = rsp.read()
    with open('./static/image/temp/background.jpg', 'wb') as f:
        f.write(img)
    while True:
        print("等待")
        if os.path.exists('./static/image/temp/background.jpg'):
            print("图片已经下载成功，返回图片！")
            return "ok"
        continue


@app.route('/upload.bf2', methods=['GET'])
def uploadBf2():
    if os.path.exists('./static/image/temp/butterfly.jpg'):
        return "exist"
    picSrc = request.args['picSrc']
    print("picSrc", picSrc)
    rsp = urllib.request.urlopen(picSrc)
    img = rsp.read()
    with open('./static/image/temp/butterfly.jpg', 'wb') as f:
        f.write(img)
    while True:
        print("等待")
        if os.path.exists('./static/image/temp/butterfly.jpg'):
            print("图片已经下载成功，返回图片！")
            return "ok"
        continue


@app.route('/show.bf', methods=['GET'])
def showBF():
    path = './static/image/white_butterfly/'
    number = str(get_number_file(path))
    print("number:", number)
    return number


@app.route('/show.ct', methods=['GET'])
def showCt():
    path = './static/image/white_cartoon/'
    number = str(get_number_file(path))
    print("number:", number)
    return number


@app.route('/upload.bf', methods=['GET'])
def uploadBf():
    if os.path.exists('./static/image/temp/butterfly.jpg'):
        return "exist"
    selectNum = request.args['selectNum']
    src = './static/image/black_butterfly/butterfly'+selectNum+'.jpg'
    dst = './static/image/temp/'
    filename = 'butterfly.jpg'
    upload_picture(src, dst, filename)
    return "ok"


@app.route('/upload.temp', methods=['GET'])
def uploadTemp():
    path = './static/image/temp/'
    fileNum = get_number_file(path)
    if fileNum == 0:
        return "none"
    if fileNum == 1:
        return "bf"
    if fileNum == 3:
        return "3"
    if fileNum == 2:
        if os.path.exists('./static/image/temp/background.jpg'):
            return "bg"
        if os.path.exists('./static/image/temp/figure.jpg'):
            return "figure"


@app.route('/filter', methods=['GET'])
def filter():
    if os.path.exists('./static/image/resultPic/filterPic.jpg'):
        os.remove('./static/image/resultPic/filterPic.jpg')
    selectNum = request.args['selectNum']
    # print("filter_selectNum", selectNum)
    # 边缘提取滤镜
    if os.path.exists('./static/image/resultPic/mixPic1.jpg'):
        if os.path.exists('./static/image/resultPic/mixPic2.jpg'):
            print("进来了")
            img = Image.open("./static/image/resultPic/mixPic2.jpg")
            img1 = cv2.imread("./static/image/resultPic/mixPic2.jpg")
            blur4 = beauty_face2(img1)
            img = img.convert("RGB")
        else:
            img = Image.open("./static/image/resultPic/mixPic1.jpg")
            img1 = cv2.imread("./static/image/resultPic/mixPic1.jpg")
            blur4 = beauty_face2(img1)
            img = img.convert("RGB")
    else:
        return "none"
    print("selectNum_type", type(selectNum))
    if selectNum == "1":
        print("进来了1")
        imgfilted_fe = img.filter(ImageFilter.FIND_EDGES)
        imgfilted_fe.save("./static/image/resultPic/filterPic.jpg")
    # 边缘增强滤镜
    if selectNum == "2":
        print("进来了2")
        imgfilted_ee_m = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        imgfilted_ee_m.save("./static/image/resultPic/filterPic.jpg")
    # 浮雕滤镜
    if selectNum == "3":
        imgfilted_em = img.filter(ImageFilter.EMBOSS)
        imgfilted_em.save("./static/image/resultPic/filterPic.jpg")
    # 轮廓滤镜
    if selectNum == "4":
        imgfilted_c = img.filter(ImageFilter.CONTOUR)
        imgfilted_c.save("./static/image/resultPic/filterPic.jpg")
    # 模糊滤镜
    if selectNum == "5":
        imgfilted_b = img.filter(ImageFilter.BLUR)
        imgfilted_b.save("./static/image/resultPic/filterPic.jpg")
    # 平滑滤镜
    if selectNum == "6":
        imgfilted_sm = img.filter(ImageFilter.SMOOTH)
        imgfilted_sm.save("./static/image/resultPic/filterPic.jpg")
    # 平滑滤镜-加强版
    if selectNum == "7":
        imgfilted_sm_m = img.filter(ImageFilter.SMOOTH_MORE)
        imgfilted_sm_m.save("./static/image/resultPic/filterPic.jpg")
    # 锐化
    if selectNum == "8":
        imgfilted_sh = img.filter(ImageFilter.SHARPEN)
        imgfilted_sh.save("./static/image/resultPic/filterPic.jpg")
    # 美白-缇庣櫧
    if selectNum == "9":
        blur4 = beauty_face2(img1)
        cv2.imwrite("./static/image/resultPic/filterPic.jpg", blur4)
   # 细节
    if selectNum == "10":
        imgfilted_d = img.filter(ImageFilter.DETAIL)
        imgfilted_d.save("./static/image/resultPic/filterPic.jpg")
    # 组合
    if selectNum == "11":
        group_imgfilted = img.filter(ImageFilter.CONTOUR)
        group_imgfilted = group_imgfilted.filter(ImageFilter.SMOOTH_MORE)
        group_imgfilted.save("./static/image/resultPic/filterPic.jpg")
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
    else:
        return "hasBf"


@app.route('/show.compareFill', methods=['GET'])
def compareFill():
    if os.path.exists('./static/image/resultPic/compareFill.jpg'):
        os.remove('./static/image/resultPic/compareFill.jpg')
    alpha = float(request.args['compareNum'])
    beta = float(request.args['fillNum'])
    path = './static/image/resultPic/'
    fileNum = get_number_file(path)
    # print("fileNum:", fileNum)
    if fileNum == 3:
        src = './static/image/resultPic/filterPic.jpg'
        img = cv2.imread(src)
        img = Contrast_and_Brightness(alpha, beta, img)
        cv2.imwrite("./static/image/resultPic/compareFill.jpg", img)
    if fileNum == 2:
        src = './static/image/resultPic/mixPic2.jpg'
        img = cv2.imread(src)
        # print("img:", img)
        # print("22222222222222")
        img = Contrast_and_Brightness(alpha, beta, img)
        cv2.imwrite(
            "./static/image/resultPic/compareFill.jpg", img)
    if fileNum == 1:
        src = './static/image/resultPic/mixPic1.jpg'
        img = cv2.imread(src)
        img = Contrast_and_Brightness(alpha, beta, img)
        cv2.imwrite("./static/image/resultPic/compareFill.jpg", img)
    if fileNum == 0:
        return "0"
    return "ok"


# 运行服务器
if __name__ == '__main__':
        # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
        # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        # SEND_FILE_MAX_AGE_DEFAULT=datetime.timedelta(seconds=1),
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
    # app.run() 开始运行服务器
    # 所以你访问下面的网址就可以打开网站了
    # http://127.0.0.1:2000/
    # lyricResult()
