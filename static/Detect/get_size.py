import cv2

def get_size(src):

    img1 = cv2.imread(src)
    height_1, width_1 = img1.shape[:2]
    print("picture_size: height为: {0},width为: {1}".format(height_1, width_1))


src = './static/image/background/taylor2_res.jpg'
get_size(src)
