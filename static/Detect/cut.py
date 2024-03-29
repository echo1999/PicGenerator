import cv2
import base64
import numpy as np

from aip import AipBodyAnalysis


def cut_picture(src):

    # 在百度云中申请，每天各接口有 500 次调用限制.
    APP_ID = '16628525'
    API_KEY = '5ioBzjijPln33f7mPzyProbc'
    SECRET_KEY = 'FR4URtsr2Q77r6RvNyld4swls1Eik5Pu'

    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

    # 读取待分割人像图片
    imgfile = src
    ori_img = cv2.imread(imgfile)
    height, width, _ = ori_img.shape

    with open(imgfile, 'rb') as fp:
        img_info = fp.read()
        # print("img_info:", img_info)

    seg_res = client.bodySeg(img_info)
    labelmap = base64.b64decode(seg_res['labelmap'])
    nparr = np.fromstring(labelmap, np.uint8)
    labelimg = cv2.imdecode(nparr, 1)
    labelimg = cv2.resize(labelimg, (width, height),
                          interpolation=cv2.INTER_NEAREST)
    new_img = np.where(labelimg == 1, 255, labelimg)
 # maskfile = imgfile.replace('.jpg', '_mask.png')
    maskfile_dir = './static/image/cut/' + \
        imgfile.split('/')[-1].split('.')[0]+'_mask.png'
    cv2.imwrite(maskfile_dir, new_img)

    # res_imgfile = imgfile.replace('.jpg', '_res.jpg')
    result = cv2.bitwise_and(ori_img, new_img)
    # 保存最终分割出的人像图片到原始图片所在目录

    result_path = './static/image/cut/' + \
        imgfile.split('/')[-1].split('.')[0]+'_res.jpg'
    cv2.imwrite(result_path, result)


# src = './static/image/temp/figure.jpg'
# cut_picture(src)
