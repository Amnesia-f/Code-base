price = 200
height = float(input("请输入身高（米）："))
if height <= 1.4:
   save = price * 0.5
   print("节省的金额（元）：", save)
else:
   save = price * (1 - 0.9)
   print("节省的金额（元）：", save)
print("实际支付金额（元）：", price - save)
