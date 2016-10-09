import time
startTime = time.clock()
limit = 1000000
total = 0
def findPrimes(limit):
    import math
    array = [True for i in range(limit + 1)]
    array[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if array[i]:
            for j in range(i * 2, limit, i):
                array[j] = False
    return array

primes = findPrimes(limit)
def isTrunc(num):
    for j in range((len(str(num)) - 1)):
        if not (primes[int(str(num)[j + 1:])] and primes[int(str(num)[:(j + 1) * -1])]):
            return False
        return True
    return False
            
for i in range(10, limit + 1):
    if primes[i]:
        if isTrunc(i):
            total += i
print("--- sum of primes is %s ---" % total)
print("--- %s seconds ---" % (time.clock() - startTime))
