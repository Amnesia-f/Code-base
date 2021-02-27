import random
times = 5
secret = random.randint(1,10)
print('------------------一个小小的游戏------------------')
guess = 0
print("不妨猜一下我现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print("这么厉害吗，你竟然猜中了？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("嘿，大了，大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")