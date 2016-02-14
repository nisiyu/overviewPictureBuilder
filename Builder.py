# coding:utf-8
__author__ = 'siyu'

from PIL import Image, ImageDraw, ImageFont
import sys

tmpimg = Image.new("RGBA",(100,60))
draw = ImageDraw.Draw(tmpimg)


class style:
    def __init__(self):
        self.height_percent = 90
        self.width_percent = 90
        self.height_margin = 5
        self.width_margin = 10
        self.fontsize = 20
        self.fonttype = "msyh.ttc"
        self.font = ImageFont.truetype(self.fonttype, self.fontsize)
        self.fontcolor = (0,0,0,0)
        self.bordertype = 0
        self.bordercolor = (0,0,0,0)
        self.fillincolor = (0,0,0,0)

class block(style):
    def __init__(self, t=""):
        style.__init__(self)
        self.title = t
        self.items = []
        self.height = 0

    def set_items(self, items):
        self.items = items

    def calc_height(self):
        global draw
        if self.items == []:
            # it's an item
            width, height = draw.textsize(self.title, font=self.font)
            self.height = height * 100 / self.height_percent
            return self.height
        else:
            height = 0
            for item in self.items:
                height += item.calc_height()
            height += (len(self.items) + 1) * self.height_margin
            title_width, title_height = draw.textsize(self.title, font=self.font)
            height += title_height * 100 / self.height_percent
            self.height = height
            return self.height



class settings(block):
    def __init__(self):
        style.__init__(self)
        self.column_width = 0
        self.column_num = 0
        self.columns = []



    def test_data(self):
        self.title = u'标题1'
        grp1 = block('title1')
        grp1.set_items([block('item111'), block('item112')])
        grp2 = block('title2')
        grp2.set_items([block('item121'), block('item122'), block('item123')])
        self.set_items([grp1, grp2])
        self.column_num = 2
        self.column_width = 100


    def calc_all_items_height(self):
        for blk in self.items:
            print blk.calc_height()


    def align_items(self):
        pass

    def draw_all(self):
        pass




def main(args):
    try:
        s = settings()
        s.test_data()
        s.calc_all_items_height()
        s.align_items()
        s.draw_all()
    except Exception as ex:
        print ex

main("")