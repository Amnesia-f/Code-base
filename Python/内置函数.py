lists = [8.8, 9.6, 7.6, 10, 8.2, 9.3, 8.5, 6.3, 7.9, 5.6]
lists.remove(max(lists))
lists.remove(min(lists))
a = sum(lists) / len(lists)
print("去掉一个最高分和一个最低分，本选手的最后得分是:", round(a, 2))
