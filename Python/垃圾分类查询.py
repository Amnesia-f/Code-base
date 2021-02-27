#导入所需模块与函数
import requests
from urllib.request import quote
import re
import tkinter as tk
import tkinter.messagebox

#网页内容的获取与匹配
def Query_operation():
    rubbish_form = input_rubbish.get()
    rubbish = quote(rubbish_form, encoding='utf-8')
    url = 'https://lajifenleiapp.com/sk/'+rubbish
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE/10.0.2032.0'}
    res = requests.get(url, headers=headers).text
    rubbish_name = '<span style="color:#D42121;">(.*?)</span>'
    rubbish_ascription = '<span style="color:#FBbC28;">&nbsp;(.*?)&nbsp;'
    rubbish_belong = '</span><span style="#2e2a2b">(.*?)</span>'
    info1 = re.findall(rubbish_name, res, re.S)
    info2 = re.findall(rubbish_ascription, res, re.S)
    info3 = re.findall(rubbish_belong, res, re.S)
    rubbish_name1.set(tuple(info1))
    rubbish_ascription1.set(tuple(info2))
    rubbish_belong1.set(tuple(info3))
    if info1:
        return
    else:
        tkinter.messagebox.showerror('错误', '没有查询到这种垃圾')

#窗口设计
window = tk.Tk()
window.title('垃圾分类查询')
window.geometry('450x150')

#窗口内组件设计
tk.Label(window, text='垃圾名称：', font=('楷体', 14)).place(x=5, y=20)

input_rubbish = tk.StringVar()
input_rubbish.set('酒瓶（示例）')
input_rubbish = tk.Entry(window, textvariable=input_rubbish, font=('楷体', 14), width = 15)
input_rubbish.place(x=100, y=20)

button_query = tk.Button(window, text='查询', font=('楷体', 11), command=Query_operation)
button_query.place(x=260, y=17)

rubbish_name1 = tk.StringVar()
r_name = tk.Label(window, fg='red', font=('楷体', 15), width=10, height=2, textvariable=rubbish_name1)
r_name.place(x=20, y=60)
rubbish_ascription1 = tk.StringVar()
r_ascription = tk.Label(window, fg='green', font=('楷体', 15), width=5, height=2, textvariable=rubbish_ascription1)
r_ascription.place(x=155, y=60)
rubbish_belong1 = tk.StringVar()
r_belong = tk.Label(window, fg='blue', font=('楷体', 15), width=15, height=2, textvariable=rubbish_belong1)
r_belong.place(x=260, y=60)

window.mainloop()
