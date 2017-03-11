import time, itertools, math
startTime = time.clock()
pans = [int("".join(i)) for i in itertools.permutations("1234567")]

def isPrime(n):
    if n == 1 or n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in reversed(pans):
    if isPrime(i):
        print i

print("--- %s seconds ---" % (time.clock() - startTime))
