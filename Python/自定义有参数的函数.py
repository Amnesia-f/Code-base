def a(n):
    for number in range(n):
        for i in range(5):
            for j in range(5 - i):
                print(" ", end = "")
            for k in range(i + 1):
                print("☆", end = "")
            print()
a(3)
