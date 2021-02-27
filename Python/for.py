money = float(input("请输入投资金额（万元）："))
for i in range(10):
    y = i + 1
    f = money * (1 + 0.05) ** y
    print("投资%d年后的本利和（万元）："%y, round(f, 2))
