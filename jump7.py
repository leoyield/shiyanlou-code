#test
maxnum = 100
l = [x for x in range(1, maxnum +1) if (x % 7 != 0 and x // 10 != 7 and x % 10 != 7)]
for i in l:
    print(i)
