from PIL import Image, ImageDraw, ImageFont

class ExtendedDraw(ImageDraw.ImageDraw):
    def __init__(self, im, mode=None):
        ImageDraw.ImageDraw.__init__(self, im, mode)

    def rectangle_radius(self, coord, radius=(0,0), fill=None, outline=None):
        x1, y1, x2, y2 = coord
        radius_x, radius_y = radius
        diameter_x = radius_x * 2
        diameter_y = radius_y * 2
        draw = self

        # main part fill in
        draw.rectangle((x1+radius_x,y1,x2-radius_x,y2), fill=fill)
        draw.rectangle((x1,y1+radius_y,x2,y2-radius_y), fill=fill)

        # border line
        draw.line((x1+radius_x,y1,
                   x2-radius_x,y1), fill=outline)
        draw.line((x1,y1+radius_y,
                   x1,y2-radius_y), fill=outline)
        draw.line((x2,y1+radius_y,
                   x2,y2-radius_y), fill=outline)
        draw.line((x1+radius_x,y2,
                   x2-radius_x,y2), fill=outline)

        # four corners fill in
        draw.pieslice((x2-diameter_x, y2-diameter_y,
                       x2, y2),
                      0,90, fill=fill)
        draw.pieslice((x1, y2-diameter_y,
                       x1+diameter_x, y2),
                      90,180, fill=fill)
        draw.pieslice((x1, y1,
                       x1+diameter_x, y1+diameter_y),
                      180,270, fill=fill)
        draw.pieslice((x2-diameter_x, y1,
                       x2, y1+diameter_y),
                      270,0, fill=fill)

        # four corners borders
        draw.arc((x2-diameter_x, y2-diameter_y,
                  x2, y2),
                 0,90, fill=outline)
        draw.arc((x1, y2-diameter_y,
                       x1+diameter_x, y2),
                      90,180, fill=outline)
        draw.arc((x1, y1,
                       x1+diameter_x, y1+diameter_y),
                      180,270, fill=outline)
        draw.arc((x2-diameter_x, y1,
                       x2, y1+diameter_y),
                      270,0, fill=outline)

def Draw(im, mode=None):
    try:
        return im.getdraw(mode)
    except AttributeError:
        return ExtendedDraw(im, mode)


def __testcase():
    black = (0,0,0,255)
    red = (255,0,0,255)
    img = Image.new("RGBA", (500,500))
    x1 = 150
    y1 = 100
    x2 = 400
    y2 = 300
    radius_x = 10
    radius_y = 15
    draw = ExtendedDraw(img)
    draw.rectangle_radius((x1, y1, x2, y2), (radius_x, radius_y), fill=red, outline=black)

    img.save("test3.png")

#__testcase()