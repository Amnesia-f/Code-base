a = float(input("请输入第一条边的边长："))
b = float(input("请输入第二条边的边长："))
c = float(input("请输入第三条边的边长："))
if a + b > c and a + c > b and b + c > a:
    print("是三角形")
if a + b <=c or a + c <= b or b + c <= a:
    print("不是三角形")
