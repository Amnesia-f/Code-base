#计算平面上两点间的直线距离
import numpy as np
import math
x1 = int(input("第一个点的横坐标："))
y1 = int(input("第一个点的纵坐标："))
x2 = int(input("第二个点的横坐标："))
y2 = int(input("第二个点的纵坐标："))
n1 = np.array([x1, y1])
n2 = np.array([x2, y2])
n3 = n2 - n1
n4 = math.hypot(n3[0], n3[1])
print("第一个点的坐标：(%d，%d)"%(x1, y1))
print("第二个点的坐标：(%d，%d)"%(x2, y2))
print("两个点间的直线距离：%f"%n4)
