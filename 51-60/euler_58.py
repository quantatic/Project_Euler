import time, math
startTime = time.clock()
lastDiag = 1
space = 2
diagonals = 1
primes = 0.0
run = True
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
i = 1

while run:
    for j in range(4):
        lastDiag += space
        if j != 3:
            if isPrime(lastDiag):
                primes += 1
        diagonals += 1
        if primes * 100 / diagonals < 10:
            print space + 1
            run = False
    space += 2
    
print ("--- %s seconds ---" % (time.clock() - startTime))
