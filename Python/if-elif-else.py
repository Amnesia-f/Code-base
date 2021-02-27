height = float(input("请输入学生的身高（米）："))
weight = float(input("请输入学生的体重（千克）："))
bmi = weight / height ** 2
print("BMI数值为：", bmi)
if bmi < 18.5:
    print("偏瘦")
elif 18.5 <= bmi < 24:
    print("正常")
elif 24 <= bmi < 28:
    print("偏胖")
else:
    print("肥胖")
