a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("能构成三角形！")
    p = (a + b + c) / 2
    s = pow(p * (p - a) * (p - b) * (p - c), 0.5)
    print("面积：", s)
else:
    print("不能构成三角形，请重新输入")