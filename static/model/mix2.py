import cv2


def mix_picture(background,figure):

    img1 = cv2.imread(background)
    img2 = cv2.imread(figure)

    height_1,width_1 = img1.shape[:2]
    height_2,width_2 = img2.shape[:2]

    # 设置roi
    # rows, cols = img2.shape[:2]
    # roi = img1[:rows, :cols]

    # 设置roi
    r1 = height_1 - height_2-70
    r2 = height_1-70
    c1 = width_1 - width_2 -300
    c2 = width_1 -300
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
    cv2.imwrite("../image/result_mix3.jpg", img1)


#背景图片
background='../image/secen.jpg'
#人像图片
figure='../image/taylor2_res.jpg'
mix_picture(background,figure)