import numpy as np
import cv2


def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    dst = cv2.addWeighted(img, alpha, blank, 1-alpha, beta)
    return dst


#α调节对比度系数，取0~3；β调节亮度，取0~255
# alpha = 1.2
# beta = 1.5

# src='./html/figure1.jpg'
# img = cv2.imread(src)
# img=Contrast_and_Brightness(alpha,beta,img)
# cv2.imwrite('./compare_fill_image/'+src.split('/')[-1], img)

