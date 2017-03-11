import time, math
startTime = time.clock()
maximum = 0
for i in range(1000000):
    tmp = 1
    for j in range(2, i):
        if i % j != 0:
            print i, j
            tmp += 1
    if float(i) / tmp > maximum:
        maximum = float(i) / tmp
    print float(i) / tmp, i
print maximum
print("--- %s seconds ---" % (time.clock() - startTime))
