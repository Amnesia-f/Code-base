import re
import jieba
import wordcloud
def getText(text):#该函数用来替换文本中出现的特殊字符
    txt = text
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~，。、 ：':
        txt = txt.replace(ch, "")   #将文本中特殊字符替换为空格
    return txt

string = open(r'C:\\Users\\Administrator\\Documents\\Tencent Files\\3586454827\\FileRecv\\白痴(1701215773).txt','r',encoding='utf-8').read()
s = re.compile('2020.+洋仔|2020.+✎﹏ℳ๓ 大大大威锅丶|表情|图片|2019.+洋仔|2019.+✎﹏ℳ๓ 大大大威锅丶|撤回了一条消息|系统消息|2020.+涂卿洋')
message = re.sub(s,'',string)
message = getText(message)
split_message = jieba.lcut(message)
wordcloud_txt = ' '.join(split_message)
w=wordcloud.WordCloud(background_color="white", font_path='./fonts/simhei.ttf',width=1600,height=800,max_words=2000)#设置生成词云的参数
w.generate(wordcloud_txt)#向词云传递文本
w.to_file("聊天记录词云.png")#最后生成词云的图片
