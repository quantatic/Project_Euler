import time, sys
startTime = time.clock()
minDif = sys.maxint
pent = set([(n * ((3 * n) - 1)) / 2 for n in range(1, 9999)])
for i in pent:
    for j in pent:
        if j - i in pent and j + i in pent:
            minDif = j - i
            print(j, i)
        else:
            continue


print("--- your answer is %s ---" % minDif)
print("--- found in %s seconds ---" % (time.clock() - startTime))
