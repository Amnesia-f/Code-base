#导入所需模块
import re
import tkinter, tkinter.messagebox
 
#创建窗口，并设置大小与标题
window = tkinter.Tk() #生成主窗口，用window表示，后面就在window操作
window.geometry('300x270+400+100') #指定主框体大小
#不允许改变窗口大小
window.resizable(False, False) #框体大小可调性，分别表示x,y方向的可变性，这里我们设置为不可调
#设置窗口标题
window.title('计算器')

#定义计算器按钮功能与不规范操作的提醒
def ButtonOperation(m):  # 定义函数名为ButtonOperation，形式参数为m
    theme = themeVar.get()  # 使用get函数获取文本框中的内容 ，再赋值给theme变量
    #如果开始的内容是以小数点开头的，则在小数点前面加“0”
    if theme.startswith('.'):
        theme = '0' + theme  # 在theme变量前加上一个“0”，再重新赋值给theme变量
    #按下不同的按钮会有不同的效果
    if m in '0123456789':
        theme += m  # 0-9中哪个键按下了，就在theme字符串中增添
    elif m == '.':
        #re.split，支持正则及多个字符切割
        Segmentationpart = re.split(r'\+|-|\*|/',theme)[-1]#将theme从+-*/这些字符的地方分割开来，[-1]表示获取最后一个字符
        if '.' in Segmentationpart:
            tkinter.messagebox.showerror('错误','重复出现的小数点')#出现对话框，并提示信息
            return
        else:
            theme += m #如果没有问题，则在theme字符串中增添
    elif m == 'C':
        theme = '' #清除文本框的内容
    elif m in operators:
        if theme.endswith(operators):#如果theme中最后出现+-*/,使用endwith函数判断字符串的结尾字符
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        theme += m
    elif m == 'Sqrt':
        n = theme.split('.') #从.处分割存入n，n是一个列表
        if all(map(lambda x:x.isdigit(),n)): #isdigit函数的作用是检测字符串是否只由数字组成。x中至少有一个字符且如果x中的所有字符都是数字，那么返回结果就是True；否则，就返回False
            theme=eval(theme)**0.5
        else:
            tkinter.messagebox.showerror('错误', '算式错误')
            return
    elif m == '=':
        try: #异常处理
            #对输入的算式求值
            theme=str(eval(theme))#调用函数eval，用字符串计算出结果
        except:
            tkinter.messagebox.showerror('错误', '算式错误')
            return
    themeVar.set(theme) #将结果显示到文本框中，使用set方法可以取值

#设置文本框的大小和位置
themeVar = tkinter.StringVar(window, '')
themeEntry = tkinter.Entry(window, textvariable=themeVar) #括号里面，可见第一个都是window,即表示都是以window为主界面的，将文本框中的内容赋给textvariable
themeEntry['state'] = 'readonly' #文本框只能读，不能写
themeEntry.place(x=10, y=10, width=280, height=20) #文本框在窗口中的xy坐标位置，以及文本框自身的宽和高
#放置10个数字、小数点和计算平方根的按钮
figure = list('0123456789.')+['Sqrt']
index = 0
#用循环的方式将上面数字、小数点、平方根这12个按钮分成四行三列进行放置
for row in range(4):#row：行
    for col in range(3):#col：列
        a = figure[index] #按索引从list中取值，和c语言中的数组类似
        index += 1 #索引号递增
        m_figure = tkinter.Button(window, text=a, command=lambda x=a:ButtonOperation(x)) #和上面的是类似的
        m_figure.place(x=20+col*70, y=80+row*50, width=50, height=20) #很显然，每次放一个按钮的位置是不一样的，但是它们之间的关系是确定的
#放置运算符按钮
operators = ('+', '-', '*', '/', '**', '//')
#enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引列表，同时列出数据和数据下标，一般用在for循环当中。
for index,operator in enumerate(operators):
    m_operator = tkinter.Button(window, text=operator, bg = 'orange', command=lambda x=operator:ButtonOperation(x))#创建的过程和上面类似
    m_operator.place(x = 230, y = 80+index*30, width = 50, height = 20)#运算符是从上至下依次摆放，故横坐标不变，纵坐标逐渐增大。
#放置清除按钮和等号按钮
m_Clear = tkinter.Button(window,text='C',bg = 'red',command=lambda:ButtonOperation('C'))#在window主界面中放置按钮，按钮上显示C，红色，点击按钮后进入ButtonOperation回调函数做进一步的处理
#下面的内容和上面的模式都是一样的
m_Clear.place(x=40,y=40,width=80,height=20)
m_EqualSign = tkinter.Button(window,text='=',bg = 'yellow',command=lambda:ButtonOperation('='))#在window主界面中放置按钮，按钮上显示=，黄色，点击按钮后进入ButtonOperation回调函数做进一步的处理
m_EqualSign.place(x=170,y=40,width=80,height=20)
 
window.mainloop() #进入消息循环（必需组件）
