#start
# -*- coding: cp936 -*-
from PIL import Image, ImageFilter
import numpy as np
import cv2


def beauty_face2(src):

    dst = np.zeros_like(src)
    # int value1 = 3, value2 = 1; ĥƤ�̶���ϸ�ڳ̶ȵ�ȷ��
    v1 = 3
    v2 = 1
    dx = v1 * 5  # ˫���˲�����֮һ
    fc = v1 * 12.5  # ˫���˲�����֮һ
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

#����
img1=cv2.imread("../image/taylor2.jpg")
blur4 = beauty_face2(img1)
cv2.imwrite("./filter/����.jpg", blur4)


##ͼ����##
#ת��ΪRGBͼ��
img = img.convert("RGB")

#����PIL�Դ�filter����
#ģ���˾�
imgfilted_b = img.filter(ImageFilter.BLUR)
imgfilted_b.save("./filter/ģ��.jpg")

#�����˾�
imgfilted_c = img.filter(ImageFilter.CONTOUR)
imgfilted_c.save("./filter/����.jpg")

#��Ե��ǿ�˾�
imgfilted_ee = img.filter(ImageFilter.EDGE_ENHANCE)
imgfilted_ee.save("./filter/��Ե��ǿ.jpg")

#��Ե��ǿ�˾�---��ǿ��
imgfilted_ee_m = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
imgfilted_ee_m.save("./filter/��Ե��ǿ.jpg")

#�����˾�
imgfilted_em = img.filter(ImageFilter.EMBOSS)
imgfilted_em.save("./filter/����.jpg")

#��Ե��ȡ�˾�
imgfilted_fe = img.filter(ImageFilter.FIND_EDGES)
imgfilted_fe.save("./filter/��Ե��ȡ.jpg")

#ƽ���˾�
imgfilted_sm = img.filter(ImageFilter.SMOOTH)
imgfilted_sm.save("./filter/ƽ��.jpg")

#ƽ���˾�������ǿ��
imgfilted_sm_m = img.filter(ImageFilter.SMOOTH_MORE)
imgfilted_sm_m.save("./filter/ƽ���˾�_��ǿ��.jpg")

#���˾�
imgfilted_sh = img.filter(ImageFilter.SHARPEN)
imgfilted_sh.save("./filter/��.jpg")

#ϸ���˾�
imgfilted_d = img.filter(ImageFilter.DETAIL)
imgfilted_d.save("./filter/ϸ��.jpg")

##���ʹ��filter
group_imgfilted = img.filter(ImageFilter.CONTOUR)
group_imgfilted = group_imgfilted.filter(ImageFilter.SMOOTH_MORE)
group_imgfilted.save("./filter/���.jpg")

