import time
startTime = time.clock()
triangle = set([(n ** 2 + n) / 2 for n in range(285, 100000)])
pent = set([(3 * n ** 2 - n) / 2 for n in range(165, 100000)])
hex = set([2 * n ** 2 - n for n in range(143, 100000)])

for i in hex:
    if i in triangle and i in pent:
        print i
print("--- %s seconds ---" % (time.clock() - startTime))

