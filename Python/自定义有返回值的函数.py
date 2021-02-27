def date(year, month, day):
    count = 0
    if year % 400 == 0 or (year % 4 == 0 and year %100 != 0):
        print("%d年是闰年，2月份有29天！"%year)
        list1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            count += list1[i]
        return count + day
    else:
        print("%d年是平年，2月份有28天！"%year)
        list2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            count += list2[i]
        return count + day
print("给定日期是当年的第%d天！"%date(2016, 6, 5))
