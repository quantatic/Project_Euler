import time
startTime = time.clock()
maximum = 0
for a in range(90, 100):
    for b in range(90, 100):
        maximum = max(sum(int(j) for j in str(a ** b)), maximum)

print maximum
print("--- %s seconds ---" % (time.clock() - startTime))
