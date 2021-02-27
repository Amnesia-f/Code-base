name_1 = input("请输入小张的存款金额：")
name_1 = float(name_1)
name_2 = input("请输入小李的存款金额：")
name_2 = float(name_2)
if name_1 > name_2:
    print("小张的存款更多")
if name_1 < name_2:
    print("小李的存款更多")
if name_1 == name_2:
    print("小张和小李的存款一样多")
