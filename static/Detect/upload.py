# coding=utf-8
import cv2

def upload_picture(src,dst):

    img1=cv2.imread(src)
    path=dst+src.split('.')[-2].split('/')[-1]+'.'+src.split('.')[-1]
    #将图片以原图命名放置到指定文件夹下
    cv2.imwrite(path,img1)


# 原图
src = './static/image/taylor2.jpg'
#目的放置位置（不包含图片名）
dst = './static/image/temp/'
upload_picture(src,dst)
