# coding=utf-8
import cv2


def upload_picture(src, dst, name):

    img1 = cv2.imread(src)
    # path=dst+src.split('.')[-2].split('/')[-1]+'.'+src.split('.')[-1]
    path = dst+name
    #将图片以原图命名放置到指定文件夹下
    cv2.imwrite(path, img1)


# # 原图
# src = './static/image/background/background1.jpg'
# #目的放置位置（不包含图片名）
# dst = './static/image/temp/'
# name = 'background.jpg'
# upload_picture(src, dst, name)
