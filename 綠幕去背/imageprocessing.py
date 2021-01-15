"""
File: imageprocessing.py
----------------------------------
This file creates a photoshopped image

Please create the folder to put all the images you will use
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.23

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(background, me_img):
    # to loop all the pixel
    for y in range(me_img.height):
        for x in range(me_img.width):
            # get the pixel of the your image with greenscreen
            me_pixel = me_img.get_pixel(x, y)
            # get the pixel of the background you want to combine
            background_pixel = background.get_pixel(x, y)
            # to caculate the average of the pixel
            avg = (me_pixel.red+me_pixel.green+me_pixel.blue)//3
            total = me_pixel.red+me_pixel.green+me_pixel.blue
            # 如果原本的照片綠色pixel值大於平均＊門檻 or 紅綠藍總值大於所設定的黑色值（以免原照黑色部分消失） ，原照pixel會被背景圖取代
            if me_pixel.green > avg*THRESHOLD and total > BLACK_PIXEL:
                me_pixel.red = background_pixel.red
                me_pixel.green = background_pixel.green
                me_pixel.blue = background_pixel.green
    return me_img


def main():

    me_img = SimpleImage('image/me.jpeg')
    me_img.show()
    background = SimpleImage('image/background.jpg')
    background.show()

    """
    The file will combine your image and the chose background picture.
    """
    me_img = SimpleImage('image/me.jpeg')
    background = SimpleImage('image/background.jpg')
    background.make_as_big_as(me_img)
    combined_img = combine(background, me_img)
    combined_img.show()

if __name__ == '__main__':
    main()
