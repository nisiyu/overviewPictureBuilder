# overviewPictureBuilder
生成全景图的生成器
用一个三级列表，加以配置，可以生成一个由不同样式矩形组成的全景图
实现了使用PIL绘制圆角矩形
=================================

## Dependencies
需要安装`PIL`的库

## How to use

1. 打开`ConfigParser.py`修改其中的配置
- `item_str` 所有标题的内容
- `column_num` 二级标题对应的列数，二级标题需要放进多少列
- `column_width` 每一列的矩形占的宽度
- `style_level1`到`style_level3`函数中的参数可以设置样式
- `hp` 当前元素高度占父元素的比例 `wp` 当前元素宽度占父元素的比例
- `hm` 高度的margin `wm` 宽度的margin
- `fsize` 字体大小 `ftype` 字体文件名字，有需要可以自己加 `fcolor` 字体颜色RGBA
- `bradius` 两个坐标是椭圆的x轴y轴半径 `bcolor` 边框颜色 `fillcolor` 填充颜色

2. 执行`main.py`

3. 输出图片示例
![example](https://raw.githubusercontent.com/nisiyu/overviewPictureBuilder/master/example.png)