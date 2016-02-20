from PIL import Image, ImageDraw, ImageFont

class ExtendedDraw(ImageDraw.ImageDraw):
    def __init__(self, im, mode=None):
        ImageDraw.ImageDraw.__init__(self, im, mode)

def Draw(im, mode=None):
    try:
        return im.getdraw(mode)
    except AttributeError:
        return ExtendedDraw(im, mode)

