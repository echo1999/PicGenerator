import cv2

#人像融合写死
def mix_picture_of_butterfly(background,butterfly):

    img1 = cv2.imread(background)
    img2 = cv2.imread(butterfly)

    height_1,width_1 = img1.shape[:2]
    height_2,width_2 = img2.shape[:2]
    print("background:",height_1,width_1)
    print("butterfly:", height_2, width_2)

    if height_2>height_1 or width_2 > width_1:
        if height_1<width_1:
            img2 = cv2.resize(img2, (int(((height_1-100) / height_2) * width_2),(height_1-100)), interpolation=cv2.INTER_CUBIC)
        if height_1>width_1:
            img2 = cv2.resize(img2, ((width_1-100),int(((width_1-100)/width_2)*height_2)), interpolation=cv2.INTER_CUBIC)

    height_3, width_3 = img2.shape[:2]
    print("new_butterfly:", height_3, width_3)


    # 设置roi
    r1 = height_1 - height_3-10
    r2 = height_1-10
    c1 = width_1 - width_3
    c2 = width_1
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
    cv2.imwrite("./static/image/resultPic/mixPic2.jpg", img1)


# #背景图片
# # background='../image/background3.jpg'
# background='./static/image/resultPic/mixPic1.jpg'

# #蝴蝶图片
# butterfly='./black_butterfly/butterfly6.jpg'
# mix_picture_of_butterfly(background,butterfly)