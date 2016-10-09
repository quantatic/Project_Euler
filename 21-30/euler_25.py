import time
startTime = time.clock()
i, j, counter = 1, 1, 2
while len(str(i)) < 1000:
    i, j, counter = i + j, i, counter + 1
print counter

print("--- %s seconds ---" % (time.clock() - startTime))
