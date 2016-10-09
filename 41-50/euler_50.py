import time, math
startTime = time.clock()
sieve = [True for i in range(10 ** 6)]
primes = []
sums = []
answer = 0
for i in range(2, 10 ** 3 + 1):
    for j in range(i * 2, 10 ** 6, i):
        sieve[j] = False
        
for i in range(2, len(sieve)):
    if sieve[i]:
        primes.append(i)

tmp = 0
for i in primes:
    sums.append(tmp)
    tmp += i
sums.append(tmp)
primes = set(primes)

for j in range(0, 10):
    for i in range(j, len(sums)):
        if sums[i] - sums[j] in primes and i - j > answer:
           answer = i - j
           print sums[i] - sums[j]
print answer    
print("--- %s seconds ---" % (time.clock() - startTime))

    


