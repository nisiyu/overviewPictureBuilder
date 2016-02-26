# coding:utf-8
import Builder
import config
item_str = config.item_str
column_num = config.column_num
column_width = config.column_width
style_funcs = config.style_funcs

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




