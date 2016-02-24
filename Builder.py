# coding:utf-8
__author__ = 'siyu'

from PIL import Image, ImageDraw, ImageFont
import extendedDraw
import sys

tmpimg = Image.new("RGBA",(100,60))
draw = extendedDraw.Draw(tmpimg)
#draw = ImageDraw.Draw(tmpimg)


class style:
    def __init__(self):
        self.setstyle()

    def setstyle(self, hp=90, wp=90, hm=5, wm=10,
                 fsize=20, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(0,0), bcolor=(0,0,0,255), fillcolor=(0,0,0,255)):
        self.height_percent = hp
        self.width_percent = wp
        self.height_margin = hm
        self.width_margin = wm
        self.fontsize = fsize
        self.fonttype = ftype
        self.font = ImageFont.truetype(self.fonttype, self.fontsize)
        self.fontcolor = fcolor
        self.border_radius = bradius
        self.bordercolor = bcolor
        self.fillincolor = fillcolor

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
            # it's a block including items
            height = 0
            # calc every blocks' height
            for item in self.items:
                height += item.calc_height()

            # add margins
            height += (len(self.items) + 1) * self.height_margin

            # add title height
            title_width, title_height = draw.textsize(self.title, font=self.font)
            height += title_height * 100 / self.height_percent
            self.height = height
            return self.height

    def draw(self, topleftcorner, drawobj, column_width):
        # draw the border
        drawobj.rectangle_radius((topleftcorner[0], topleftcorner[1],
                           topleftcorner[0] + column_width, topleftcorner[1] + self.height),
                                 self.border_radius,
                          fill=(0,0,0,0),
                          outline=self.bordercolor)

        # title text-align to center
        titlewidth, titleheight = drawobj.textsize(self.title, font=self.font)
        offset = 0
        #if len(self.items) > 0:
        offset = (column_width - titlewidth) / 2
        drawobj.text((topleftcorner[0] + offset,
                     topleftcorner[1]),
                     self.title,
                     font=self.font,
                     fill=self.fontcolor)
        paddingwidth = (100 - self.height_percent) * column_width / 200
        paddingheight = (100 - self.width_percent) * self.height / 200
        coord = (topleftcorner[0] + paddingwidth,
                 topleftcorner[1] + titleheight + paddingheight + self.height_margin)

        for item in self.items:
            item.draw(coord, drawobj, self.width_percent*column_width/100)
            coord = (coord[0], coord[1] + item.height + item.height_margin)




class settings(block):
    def __init__(self, colnum, colwidth):
        style.__init__(self)
        self.column_width = colwidth
        self.column_num = colnum
        self.columns = [[] for i in range(self.column_num)]
        self.columnusedheight = [0] * self.column_num


    #
    # def test_data(self):
    #     self.title = u'标题1'
    #     grp1 = block('title1')
    #     grp1.set_items([block('item111'), block('item112')])
    #     grp2 = block('title2')
    #     grp2.set_items([block('item121'), block('item122'), block('item123')])
    #     self.set_items([grp1, grp2])
    #     self.column_num = 2
    #     self.columns = [[] for i in range(self.column_num)]
    #     self.columnusedheight = [0] * self.column_num
    #     self.column_width = 100


    def calc_all_items_height(self):
        for blk in self.items:
            blk.calc_height()


    def align_items(self):
        self.items.sort(key=lambda x:-x.height)

        for blk in self.items:
            # find the shortest column index
            minh_index = self.columnusedheight.index(min(self.columnusedheight))

            # add height
            self.columns[minh_index].append(blk)
            self.columnusedheight[minh_index] += blk.height + self.height_margin

        self.height = max(self.columnusedheight) + \
                      draw.textsize(self.title,font=self.font)[1] + \
                      self.height_margin


    def draw_all(self):
        result_width = self.column_num * self.column_width + (self.column_num + 1) * self.width_margin
        result_height = self.height
        result_img = Image.new("RGBA", (result_width, result_height))
        result_draw = extendedDraw.Draw(result_img)
        coordinate = (0,0)

        # draw the border
        result_draw.rectangle((coordinate[0],coordinate[1],result_width - 1,result_height - 1),
                              fill=(0,0,0,0),
                              outline=self.bordercolor)
        result_draw.text(coordinate, self.title, font=self.font, fill=self.fillincolor)

        for i, column in enumerate(self.columns):
            # every column's top left corner
            tmp_coord = (self.width_margin + (self.width_margin + self.column_width)*i,
                         draw.textsize(self.title,font=self.font)[1] + self.height_margin)

            # to draw every block
            blk_coord = (tmp_coord[0], tmp_coord[1])
            for j, block in enumerate(column):
                block.draw(blk_coord, result_draw, self.column_width)
                blk_coord = (blk_coord[0], blk_coord[1] +
                             block.height +
                             block.height_margin)

        result_img.save("test2.png")
