def bubble_sort(lists):
    for i in range(len(lists) - 1):
        for j in range(len(lists) - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists
lists = [98, 90, 82, 95, 88]
print("要排序的列表：", lists)
print("冒泡排序结果：", bubble_sort(lists))
