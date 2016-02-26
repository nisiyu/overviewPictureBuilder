# coding:utf-8
item_str=u'''
# 安全技能 @style1
## 编程 @style2
### C
### Python
### Java
### PHP
## 搜集信息
### nmap
### GoogleHacking
### Nessus
## web工具
### Burp
### sqlmap
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