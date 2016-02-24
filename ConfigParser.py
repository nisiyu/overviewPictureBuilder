# coding:utf-8
import json
import Builder
import pprint
__author__ = 'siyu'

def Parse():
    column_num = 2
    column_width = 100
    contents_str = u'''
# 标题 @style1
## title1 @style2
### item111
### item112
## title2
### item121
### item122
### item123
'''
    stack = []
    for line in contents_str.split('\n'):
        if len(line) == 0:
            continue
            # level1
        if line.startswith("# "):
            elem = Builder.settings(column_num, column_width)
            elem.title = FindEmpty(line, 1)
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




