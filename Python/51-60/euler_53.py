import time, math
startTime = time.clock()
factorial = [math.factorial(i) for i in range(101)]
total = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        if factorial[n] / (factorial[r] * factorial[n - r]) > 10 ** 6:
            total += 1
            
print total
print("--- %s seconds ---" % (time.clock() - startTime))
