'''
*useage:
fron trans_style import sty_it
sty_it(input_img, output_img, model_checkpoint)

input_img -> 原图像路径+输入图像文件名
output_img -> 生成图路径+输出图像文件名
model_checkpoint —> 风格模型文件

'''
import keras
import numpy
import PIL.Image
import keras_contrib

# from static.Detect.layers import(
#     DeprocessStylizedImage
# )
import static.Detect.layers as layers
import static.Detect.utils as utils
# from static.Detect.utils import(
#     load_image
# )


def sty_it(input_img, output_img, model_checkpoint):
    
    custom_objects = {
        'InstanceNormalization':
            keras_contrib.layers.InstanceNormalization,
        'DeprocessStylizedImage': layers.DeprocessStylizedImage
        }
    transfer_net = keras.models.load_model(
        model_checkpoint,
        custom_objects=custom_objects
        )

    image_size = transfer_net.input_shape[1:3]

    inputs = [transfer_net.input, keras.backend.learning_phase()]
    outputs = [transfer_net.output]

    transfer_style = keras.backend.function(inputs, outputs)

    input_image = utils.load_image(
        input_img,
        image_size[0],
        image_size[1],
        expand_dims=True
    )
    output_image = transfer_style([input_image, 1])[0]
    output_image = PIL.Image.fromarray(numpy.uint8(output_image[0]))
    img=PIL.Image.open(input_img)
    height, width = img.size
    output_image = output_image.resize((height, width), PIL.Image.ANTIALIAS)
    output_image.save(output_img, quality=100)


#default
# input_img = './static/image/filter/figure1.jpg'
# output_img = './static/image/figure1.jpg'

#kela滤镜
# model_checkpoint1 = './static/Detect/滤镜/style_model/kaleidoscope_512x512_10_00015.h5'
# sty_it(input_img, output_img, model_checkpoint1)

# #notre滤镜
# model_checkpoint2 = './static/Detect/滤镜/style_model/notre_dame_512_10_00015.h5'
# sty_it(input_img, output_img, model_checkpoint2)

# #head_of_clown滤镜
# model_checkpoint3 = './static/Detect/滤镜/style_model/head_of_clown_512_10_00015.h5'
# sty_it(input_img, output_img, model_checkpoint3)
