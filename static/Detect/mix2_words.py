import cv2


def mix_picture_of_words(x,y,size,background,butterfly):

    img1 = cv2.imread(background)
    img2 = cv2.imread(butterfly)
    # print("img1",img1)
    # print("img2",img2)
    height_1,width_1 = img1.shape[:2]
    height_2,width_2 = img2.shape[:2]
    print("background:",height_1,width_1)
    print("butterfly:", height_2, width_2)

    # if height_2>height_1 or width_2 > width_1:
    #     if height_1<width_1:
    #         img2 = cv2.resize(img2, (int(((height_1-100) / height_2) * width_2),(height_1-100)), interpolation=cv2.INTER_CUBIC)
    #     if height_1>width_1:
    #         img2 = cv2.resize(img2, ((width_1-100),int(((width_1-100)/width_2)*height_2)), interpolation=cv2.INTER_CUBIC)

    img2 = cv2.resize(img2,(int(144*size),int(144*size)),)
    height_3, width_3 = img2.shape[:2]
    print("new_butterfly:", height_3, width_3)

    #设置roi区域
    r1=y
    r2=y+width_3
    c1=x
    c2=x+height_3
    roi = img1[r1:r2,c1:c2]


    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  #转换成灰度图像
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img1_bg, img2)  # 进行融合
    img1[r1:r2,c1:c2]=dst

    #保存融合后的图片
    cv2.imwrite("./static/image/resultPic/words.jpg", img1)


#背景图片
# background='./static/image/background/background3.jpg'
# #人像图片
# butterfly='./static/image/black_butterfly/butterfly14.jpg'
# x=60  #x坐标
# y=70  #y坐标
# size=100
# size=size/100
# mix_picture_of_butterfly(x,y,size,background,butterfly)