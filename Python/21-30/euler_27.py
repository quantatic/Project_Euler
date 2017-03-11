import time
import math
startTime = time.clock()
maxA = 0
maxB = 0
maxCount = 0
def isPrime(number):
    if number < 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        counter = 0
        while isPrime(counter ** 2 + counter * a + b):
            counter = counter + 1
        if counter > maxCount:
            maxCount = counter
            maxA = a
            maxB = b

print maxA
print maxB
print maxA * maxB
print("--- %s seconds ---" % (time.clock() - startTime))
        


