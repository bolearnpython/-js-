# 字体反爬虫 获取每个页面对应的字体映射  获取字体得到映射关系
# 汽车之家
from fontTools.ttLib import TTFont
font = TTFont('autohome.ttf')
uniList = font['cmap'].tables[0].ttFont.getGlyphOrder()
utf8List = [uni[3:] for uni in uniList[1:]]
wordList = ['一', '七', '三', '上', '下', '不', '九', '了', '二', '五', '低', '八', '六', '十', '的',
            '着', '近', '远', '长', '右', '呢', '和', '四', '地', '坏', '多', '大', '好', '小', '少',
            '短', '矮', '高', '左', '很', '得', '是', '更']
font_dict = dict(zip(utf8List, wordList))
print(font_dict)

# 去哪儿
from fontTools.ttLib import TTFont
font = TTFont('autohome2.ttf')
uniList = font['cmap'].tables[0].ttFont.getGlyphOrder()[1:]
font_dict = dict((v, str(k)) for k, v in enumerate(uniList))

old_num = '549'
new_num = ''.join(font_dict[i] for i in old_num)
print(new_num)
