# coding:utf-8
item_str=u'''
# 标题 @style1
## title1 @style2
### item111
### item112
### item113
### item114
### item115
### item116
### item117
### item118
### item119
## title2
### item121
### item122
### item123
## title3
### item131
### item132
'''
column_num = 2
column_width = 400

def style_level1(obj):
    obj.setstyle(hp=90, wp=90, hm=10, wm=10,
                 fsize=30, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(5,5), bcolor=(0,0,0,255), fillcolor=(255,255,204,255))

def style_level2(obj):
    obj.setstyle(hp=90, wp=90, hm=10, wm=10,
                 fsize=30, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(5,5), bcolor=(0,0,0,255), fillcolor=(255,204,204,255))

def style_level3(obj):
    obj.setstyle(hp=90, wp=70, hm=5, wm=10,
                 fsize=20, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(5,5), bcolor=(0,0,0,255), fillcolor=(204,255,255,255))

style_funcs = [style_level1, style_level2, style_level3]