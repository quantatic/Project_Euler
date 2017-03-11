import time
startTime = time.clock()
maxNum = 1000
primesArray = [True for i in range(maxNum)]
primes = []
for i in xrange(2, maxNum):
    for j in xrange(i * 2, maxNum, i):
        primesArray[j] = False
for i in range(2, len(primesArray)):
    if primesArray[i]:
        primes.append(i)
primes = set(primes)
squares = [2 * i ** 2 for i in xrange(maxNum)]
oddsTest = [False for i in xrange(maxNum ** 2)]
odds = set([i * 2 + 1 for i in xrange(maxNum ** 2)])
for i in primes:
    for j in squares:
        if i + j in odds:
            oddsTest[(i + j - 1) / 2] = True
        if i + j > (len(oddsTest) * 2 + 1):
            break
for i in range(len(oddsTest)):
    if oddsTest[i] == False and (i * 2 + 1) not in primes and i > 0:
        print("--- your answer is %s ---" % (i * 2 + 1))
        break
print("--- %s seconds ---" % (time.clock() - startTime))
