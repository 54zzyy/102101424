import jieba
import wordcloud
import imageio
img = imageio.imread('苹果.png')
#读取
f = open('弹幕.txt', encoding='utf-8')
text = f.read()
#分词
text_list = jieba.lcut(text)
print(text_list)
#列表变成字符串
text_str = ' '.join(text_list)
print(text_str)
#词云图配置
wc = wordcloud.WordCloud(
    width=500,
    height=500,
    background_color='white',
    mask=img,
    font_path='msyh.ttc'
)
wc.generate(text_str)
wc.to_file('词云图.png')