import time, itertools, math

   
length = 6
maximum = 10 ** length
primes = []
sieve = [True for i in range(maximum)] #true if we have a prime number
maxFamilySize = 0
maxFamilyPrime = 0
strRange = [str(_) for _ in range(10)]
startTime = time.clock()
for i in range(2, maximum):
    for j in range(i * 2, maximum, i):
        if sieve[j]:
            sieve[j] = False

for i in range(2, maximum):
    if sieve[i] and len(str(i)) == length:
        primes.append(str(i))
        
     
primes = set(primes)

for i in primes:
    for j in [str(_) for _ in range(3)]:
        if j in i and not i[-1] == j:
            i = i.replace(j, ".")
            familySize = 0
            for k in strRange:
                if i.replace(".", k) in primes:
                    familySize += 1
            if familySize > maxFamilySize:
                maxFamilySize = familySize
                maxFamilyPrime = i.replace(".", j)
print maxFamilyPrime
print("--- %s seconds ---" % (time.clock() - startTime))
            

        
    
    


