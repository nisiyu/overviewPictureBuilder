# coding:utf-8
import Builder

item_str=u'''
# 标题 @style1
## title1 @style2
### item111
### item112
## title2
### item121
### item122
### item123
'''
column_num = 2
column_width = 400

def style_level1(obj):
    obj.setstyle(hp=90, wp=90, hm=5, wm=10,
                 fsize=30, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(5,5), bcolor=(0,0,0,255), fillcolor=(255,255,204,255))

def style_level2(obj):
    obj.setstyle(hp=90, wp=90, hm=5, wm=10,
                 fsize=30, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(5,5), bcolor=(0,0,0,255), fillcolor=(255,204,204,255))

def style_level3(obj):
    obj.setstyle(hp=90, wp=70, hm=5, wm=10,
                 fsize=20, ftype='msyh.ttc', fcolor=(0,0,0,255),
                 bradius=(5,5), bcolor=(0,0,0,255), fillcolor=(204,255,255,255))

style_funcs = [style_level1, style_level2, style_level3]

def Parse():

    contents_str = item_str
    stack = []
    for line in contents_str.split('\n'):
        if len(line) == 0:
            continue
            # level1
        if line.startswith("# "):
            elem = Builder.settings(column_num, column_width)
            elem.title = FindEmpty(line, 1)
            style_funcs[0](elem)
            id = line.rfind('@')
            if id >= 0:
                stylekey = line[id+1:]
                # todo set stylekey
            stack.append({'obj': elem, 'level': 1})

        # level2 or level3
        if line.startswith("## "):
            block_level = 2
            ItemMerge(stack, 3)

        elif line.startswith("### "):
            block_level = 3
        else:
            continue

        title = FindEmpty(line, block_level)
        elem = Builder.block(title)
        style_funcs[block_level-1](elem)
        id = line.rfind('@')
        if id >= 0:
            stylekey = line[id+1:]
            # todo set stylekey
        stack.append({'obj': elem, 'level':block_level})

    ItemMerge(stack, 3)
    ItemMerge(stack, 2)
    return stack[0]['obj']

def FindEmpty(line, block_level):
    lastindex = line.find(' ', block_level + 1)
    if lastindex == -1:
        return line[block_level + 1:]
    return line[block_level + 1:lastindex]

def ItemMerge(stack, block_level):
    itemset = []
    while stack[-1]['level'] == block_level:
        itemset.insert(0, stack[-1]['obj'])
        del stack[-1]
    if itemset:
        stack[-1]['obj'].set_items(itemset)




