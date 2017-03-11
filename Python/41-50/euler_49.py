import time, itertools
startTime = time.clock()
max = 10000
primes = []
sieve = [True for i in range(max)]
for i in range(2, max):
    if sieve[i]:
        for j in range(i * 2, max, i):
            sieve[j] = False

for i in range(1000, max):
    if sieve[i]:
        primes.append(i)
primes = set(primes)


for i in range(1000, max):
    if i in primes and i + 3330 in primes and i + 6660 in primes and not i == 1487 and all([j in str(i + 3330) and j in str(i + 6660) for j in str(i)]): #fairly long and complex logic for testing if primes are permuations of each other
        print("your answer is: " + str(i) + str(i + 3330) + str(i + 6660))
print("--- %s seconds ---" % (time.clock() - startTime))
