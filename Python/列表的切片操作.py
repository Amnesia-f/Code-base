list1 = ["汉堡", "比萨饼", "鸭肉卷", "鸡肉卷"]
list2 = ["香辣鸡翅", "烤翅", "香骨鸡", "大排鸡"]
list3 = ["红茶", "乌龙茶", "豆浆", "果汁", "可乐"]
item1 = list1[2]
print(item1)
item2 = list2[2:]
print(item2)
item3 = list3[-1]
print(item3)
lists = [item1] + item2 + [item3]
print(lists)

