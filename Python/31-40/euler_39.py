import time, math
startTime = time.clock()
maxCombo = 0
maxP = 0
squares = set([i ** 2 for i in range(1000)])
for p in range(1, 1001):
    tmp = 0
    for a in range(1, p / 2):
        for b in range(a, p / 2):
            if a ** 2 + b ** 2 in squares:
                if a + b + math.sqrt(a ** 2 + b ** 2) == p:
                    tmp += 1
    if tmp > maxCombo:
        maxP = p
        maxCombo = tmp
        print tmp
print("--- %s is the max ---" % maxP)
print("--- %s seconds ---" % (time.clock() - startTime)) #meh, just under 10 seconds. Need to improve optimization for the future...
