temp = float(input("请输入温度（℃）："))
speed = float(input("请输入风速（米/秒）："))
if temp >= 25:
    if speed >= 8:
        print("天气热且刮风")
    else:
        print("天气热且不刮风")
if temp < 25:
    if speed >= 8:
        print("天气冷且刮风")
    else:
        print("天气冷且不刮风")
