#判断输入的正整数是不是回文数
num = int(input("请输入一个正整数："))
num_r = str(num)[::-1]
print(str(num), num_r)
if str(num) == num_r:
    print("是回文数")
if str(num) != num_r:
    print("不是回文数")
