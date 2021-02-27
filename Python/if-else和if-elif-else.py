import random
computer = random.randint(0, 2)
player = int(input("请输入【石头(0)、剪刀(1)、布(2)】："))
if 0 <= player <= 2:
    if (((player == 0) and (computer == 1)) or
        ((player == 1) and (computer == 2)) or
        ((player == 2) and (computer == 0))):
        print("玩家获胜，恭喜！")
    elif player == computer:
        print("平手！")
    else:
        print("玩家输了，再接再厉！")
else:
    print("输入错误")
