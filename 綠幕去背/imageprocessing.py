"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.23

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(background, me_img):
    for y in range(me_img.height):
        for x in range(me_img.width):
            me_pixel = me_img.get_pixel(x, y)
            background_pixel = background.get_pixel(x, y)
            avg = (me_pixel.red+me_pixel.green+me_pixel.blue)//3
            total = me_pixel.red+me_pixel.green+me_pixel.blue
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
    background.make_as_big_as(me_img)
    combined_img = combine(background, me_img)
    combined_img.show()

if __name__ == '__main__':
    main()
