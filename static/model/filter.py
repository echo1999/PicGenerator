#start
# -*- coding: cp936 -*-
from PIL import Image, ImageFilter
import numpy as np
import cv2


def beauty_face2(src):

    dst = np.zeros_like(src)
    # int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
    v1 = 3
    v2 = 1
    dx = v1 * 5  # 双边滤波参数之一
    fc = v1 * 12.5  # 双边滤波参数之一
    p = 0.1

    temp4 = np.zeros_like(src)

    temp1 = cv2.bilateralFilter(src, dx, fc, fc)
    temp2 = cv2.subtract(temp1, src)
    temp2 = cv2.add(temp2, (10, 10, 10, 128))
    temp3 = cv2.GaussianBlur(temp2, (2 * v2 - 1, 2 * v2 - 1), 0)
    temp4 = cv2.subtract(cv2.add(cv2.add(temp3, temp3), src), (10, 10, 10, 255))

    dst = cv2.addWeighted(src, p, temp4, 1 - p, 0.0)
    dst = cv2.add(dst, (10, 10, 10, 255))
    return dst


img = Image.open("../image/taylor2.jpg")

#美颜
img1=cv2.imread("../image/taylor2.jpg")
blur4 = beauty_face2(img1)
cv2.imwrite("./filter/美白.jpg", blur4)


##图像处理##
#转换为RGB图像
img = img.convert("RGB")

#经过PIL自带filter处理
#模糊滤镜
imgfilted_b = img.filter(ImageFilter.BLUR)
imgfilted_b.save("./filter/模糊.jpg")

#轮廓滤镜
imgfilted_c = img.filter(ImageFilter.CONTOUR)
imgfilted_c.save("./filter/轮廓.jpg")

#边缘增强滤镜
imgfilted_ee = img.filter(ImageFilter.EDGE_ENHANCE)
imgfilted_ee.save("./filter/边缘增强.jpg")

#边缘增强滤镜---增强版
imgfilted_ee_m = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
imgfilted_ee_m.save("./filter/边缘增强.jpg")

#浮雕滤镜
imgfilted_em = img.filter(ImageFilter.EMBOSS)
imgfilted_em.save("./filter/浮雕.jpg")

#边缘提取滤镜
imgfilted_fe = img.filter(ImageFilter.FIND_EDGES)
imgfilted_fe.save("./filter/边缘提取.jpg")

#平滑滤镜
imgfilted_sm = img.filter(ImageFilter.SMOOTH)
imgfilted_sm.save("./filter/平滑.jpg")

#平滑滤镜——加强版
imgfilted_sm_m = img.filter(ImageFilter.SMOOTH_MORE)
imgfilted_sm_m.save("./filter/平滑滤镜_加强版.jpg")

#锐化滤镜
imgfilted_sh = img.filter(ImageFilter.SHARPEN)
imgfilted_sh.save("./filter/锐化.jpg")

#细节滤镜
imgfilted_d = img.filter(ImageFilter.DETAIL)
imgfilted_d.save("./filter/细节.jpg")

##组合使用filter
group_imgfilted = img.filter(ImageFilter.CONTOUR)
group_imgfilted = group_imgfilted.filter(ImageFilter.SMOOTH_MORE)
group_imgfilted.save("./filter/组合.jpg")

