import time        
b = input("请输入您的出生日期，如（20060101）：")
a = time.time()       
x = time.mktime(time.strptime(b, "%Y%m%d"))       
c = a - x      
m = c / 60
h = m / 60
d = h / 24
y = d / 365   
print("您已经活了\n", int(c), "秒\n", int(m), "分钟\n", int(h), "小时\n", int(d), "天\n", round(y, 2), "年")
