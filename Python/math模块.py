import math
r = float(input("请输入圆的半径：")) 
c = 2 * math.pi * r
s = math.pi * math.pow(r, 2)
print("圆的周长为：", round(c, 2))
print("圆的面积为：", round(s, 2))
