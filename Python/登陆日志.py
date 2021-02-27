import time

def show_info():
    print('''输入提示数字，执行相应操作
0：退出
1：查看登录日志
    ''')

def write_loginfo(username):
    """
    将用户名和登录时间写入日志
    :param username: 用户名
    """
    with open('log.txt','a') as f:
        string = "用户名：{} 登录时间：{}\n".format(username ,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        f.write(string)

def read_loginfo():
    """
    读取日志
    """
    with open('log.txt','r') as f:
        while True:
            line = f.readline()
            if line == '':
                break  # 跳出循环
            print(line)  # 输出一行内容

if __name__ == "__main__":
    # 输入用户名
    username = input('请输入用户名：')
    # 检测用户名
    while len(username) < 2 :
        print('用户名长度应不少于2位')
        username = input('请输入用户名：')
    # 输入密码
    password = input('请输入密码：')
    # 检测密码
    while len(password) < 6 :
        print('密码长度应不少于6位')
        password = input('请输入密码：')

    print('登录成功')
    write_loginfo(username)  # 写入日志
    show_info()              # 提示信息
    num = int(input('输入操作数字:')) # 输入数字
    while True:
        if num == 0:
            print('退出成功')
            break
        elif num == 1:
            print('查看登录日志')
            read_loginfo()
            show_info()
            num = int(input('输入操作数字:'))
        else:
            print('您输入的数字有误')
            show_info()
            num = int(input('输入操作数字:'))