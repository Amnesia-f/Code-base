a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (b ** 2 - 4 * a * c) >= 0:
    print("这个方程有根！")
    x1 = (-b + pow((b ** 2 - 4 * a * c), 0.5)) / (2 * a)
    x2 = (-b - pow((b ** 2 - 4 * a * c), 0.5)) / (2 * a)
    print("该方程的两个根为", x1, "和", x2)
else:
    print("该方程没有根，请重新输入")
