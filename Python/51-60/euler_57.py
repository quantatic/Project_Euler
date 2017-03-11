import time
startTime = time.clock()
num = 1
denom = 2
total = 0
for i in range(1000):
    if len(str(num + denom)) > len(str(denom)): #don't even question this algorithm
        total += 1
    num += denom * 2
    num, denom = denom, num #swaps the numerator and denominator, equal to 1/(num/denom)
print total
print("--- %s seconds ---" % (time.clock() - startTime))
    
