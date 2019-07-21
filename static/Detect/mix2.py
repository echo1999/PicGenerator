import cv2


def mix_picture(background,figure):

    img1 = cv2.imread(background)
    img2 = cv2.imread(figure)

    height_1,width_1 = img1.shape[:2]
    height_2,width_2 = img2.shape[:2]
    print("background:",height_1,width_1)
    print("figure:", height_2, width_2)

    if height_2>height_1 or width_2 > width_1:
        if height_1 < width_1:
            img2 = cv2.resize(img2, (int(((height_1-100) / height_2) * width_2),(height_1-100)), interpolation=cv2.INTER_CUBIC)
        if height_1 > width_1:
            img2 = cv2.resize(img2, ((width_1-100),int(((width_1-100)/width_2)*height_2)), interpolation=cv2.INTER_CUBIC)

    height_3, width_3 = img2.shape[:2]
    print("new_figure:", height_3, width_3)

    # 设置roi
    # rows, cols = img2.shape[:2]
    # roi = img1[:rows, :cols]

    # 设置roi
    r1 = height_1 - height_3
    r2 = height_1
    c1 = width_1 - width_3 -230
    c2 = width_1 -230
    roi = img1[r1:r2, c1:c2]

    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img1_bg, img2)  # 进行融合

    #img1[:rows, :cols] = dst  # 融合后放在原图上
    img1[r1:r2, c1:c2] = dst  # 融合后放在原图上

    #保存融合后的图片
    cv2.imwrite("./static/image/resultPic/result_mix3.jpg", img1)


#背景图片
background='./static/image/background/background1.jpg'
#人像图片
figure = './static/image/figure/figure1.jpg'
mix_picture(background,figure)
