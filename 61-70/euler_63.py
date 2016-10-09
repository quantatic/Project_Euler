import time
startTime = time.clock()
total = 0
i = 1
while i < 25:
    for j in range(1, 10):
        if len(str(j ** i)) == i:
            total += 1
    i += 1
print total
print("--- %s seconds ---" % (time.clock() - startTime))
