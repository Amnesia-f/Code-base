import random
n = random.randint(0, 100)
while True:
    ni = int(input("输入猜的数字："))
    if ni > n:
        print("大了")
        continue
    elif ni < n:
        print("小了")
        continue
    else:
        print("猜对了")
        break
