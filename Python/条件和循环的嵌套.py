cycle = 0 
num_end = 1 
while cycle < 5:
    num_rest = 4 * num_end
    for cycle in range(5):
        if(num_rest % 4 != 0):
            break
        else:
            cycle += 1
        num_rest = num_rest / 4 * 5 + 1
    num_end += 1 
print("最开始的桃子个数：", int(num_rest)) 
