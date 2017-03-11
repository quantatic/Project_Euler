import time, itertools
startTime = time.clock()
f = open('C:\Users\Aidan\Desktop\primes.txt', 'r')
primes = []
smallest = 99999999
for i in f:
    primes.append(i.replace('\n', ''))
    
smallPrimes = []
for i in primes:
    if int(i) < 10 ** 4:
        smallPrimes.append(i)
    else:
        break

primes = set(primes)
print "setup done"
for a in range(len(smallPrimes)):
    for b in range(a, len(smallPrimes)):
        if not (smallPrimes[a] + smallPrimes[b] in primes and smallPrimes[b] + smallPrimes[a] in primes):
            continue
        for c in range(b, len(smallPrimes)):
            if not (smallPrimes[a] + smallPrimes[c] in primes and smallPrimes[c] + smallPrimes[a] in primes and smallPrimes[b] + smallPrimes[c] in primes and smallPrimes[c] + smallPrimes[b] in primes):
                continue
            for d in range(c, len(smallPrimes)):
                if not (smallPrimes[a] + smallPrimes[d] in primes and smallPrimes[d] + smallPrimes[a] in primes and smallPrimes[d] + smallPrimes[b] in primes and smallPrimes[b] + smallPrimes[d] in primes and smallPrimes[d] + smallPrimes[c] in primes and smallPrimes[c] + smallPrimes[d] in primes):
                    continue
                for e in range(d, len(smallPrimes)):
                    if not (smallPrimes[a] + smallPrimes[e] in primes and smallPrimes[e] + smallPrimes[a] in primes and smallPrimes[b] + smallPrimes[e] in primes and smallPrimes[e] + smallPrimes[b] in primes and smallPrimes[e] + smallPrimes[c] in primes and smallPrimes[c] + smallPrimes[e] in primes and smallPrimes[e] + smallPrimes[d] in primes and smallPrimes[d] + smallPrimes[e] in primes):
                        continue
                    if int(smallPrimes[a]) + int(smallPrimes[b]) + int(smallPrimes[c]) + int(smallPrimes[d]) + int(smallPrimes[e]) < smallest:
                        smallest = int(smallPrimes[a]) + int(smallPrimes[b]) + int(smallPrimes[c]) + int(smallPrimes[d]) + int(smallPrimes[e])
print smallest
                    

print("--- %s seconds ---" % (time.clock() - startTime))
