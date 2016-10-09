import time, math
startTime = time.clock()
total = 0

sieve = [True for i in range(1000000)]
for i in range(2, int(math.sqrt(1000000)) + 1):
    if sieve[i]:
        for j in range(i * 2, 1000000, i):
            sieve[j] = False
print sieve[2]
print sieve[12]
print sieve[9974]
def rotate(num):
    return(int(str(num)[1:] + str(num)[0]))

def isPrime(num):
    if sieve[num]:
        return True
    else:
        return False

def checkRotations(num):
    if "0" in str(num):
        return False
    for i in range(len(str(num)) + 1):
        if not isPrime(num):
            return False
        num = rotate(num)
    return True
    
for i in range(2, 1000000):
    if checkRotations(i):
        total = total + 1 #if we got through all rotations without reaching break
        print i
print("--- %s primes ---" % total)
print("--- %s seconds ---" % (time.clock() - startTime))
    
