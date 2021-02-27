import random                                  #import代表导入模块，random是随机数模块
lost = 0
win = 0
ping = 0
while True:                    #循环
    print('='*60)
    print('****************欢迎来猜拳*****************')
    print('赢：%s      平：%s       输：%s' % (win,ping,lost))
    print('1.石头  2.剪刀   3.布  4.退出')
    robot = random.choice( ['剪刀','石头','布'])
    h = input('请出：')
    if (h == '1' and robot == '剪刀')or (h == '2' and robot == '布') or (h== '3' and robot == '石头'):             #赢
        win+=1
        print('you are the winner')
    elif (h == '1' and robot == '石头')or (h == '2' and robot == '剪刀') or (h== '3' and robot=='布'):             #平
        ping+=1
        print('ping')
    elif (h == '1' and robot == '布') or (h == '2' and robot == '石头') or (h == '3' and robot=='剪刀'):           #输
        lost+=1
        print('you are loser')
    elif h == '4':
        print('退出系统')
        break                               #退出循环
    else:
        print('输入错误，请重新输入')