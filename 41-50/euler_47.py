import time, math
startTime = time.clock()
def primes(n):
    factors = []
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            factors.append(i)
            n /= i
    if n > 1:
        factors.append(n)
    return len(set(factors))

for i in xrange(10 ** 6):
    if all(primes(j) == 4 for j in range(i, i + 4)):
        print i
        break
print("--- %s seconds ---" % (time.clock() - startTime))

