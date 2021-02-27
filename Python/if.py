h_1 = int(input("请输入第一个学生的身高（厘米）："))
n_1 = input("请输入第一个学生的姓名：")
h_2 = int(input("请输入第二个学生的身高（厘米）："))
n_2 = input("请输入第二个学生的姓名：")
h_3 = int(input("请输入第三个学生的身高（厘米）："))
n_3 = input("请输入第三个学生的姓名：")
max_h = h_1
max_n = n_1
if h_2 > max_h:
    max_h = h_2
    max_n = n_2
if h_3 > max_h:
    max_h = h_3
    max_n = n_3
print("身高最高的学生是", max_n, "身高是", max_h, "厘米")
