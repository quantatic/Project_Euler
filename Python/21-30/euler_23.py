from math import sqrt
import time
startTime = time.clock()
nonAbundant = [True for i in range(28124)]
total = 0
abundantNumbers = []
def sumOfFactors(number):
    result = [1]
    for i in range(1, int(sqrt(number) + 1)):
        if number % i == 0 and i != 1:
            result.append(i)
            if number / i != i:
                result.append(number / i)
    return sum(result)


for i in range(2, 28124):
    if sumOfFactors(i) > i:
        abundantNumbers.append(i)
        
for i in abundantNumbers:
    for j in abundantNumbers:
        if i + j <= 28123:
            nonAbundant[i + j] = False
        else:
            break

for i in range(0, 28124):
    if nonAbundant[i] == True:
        total = total + i
    
print total
print ("--- %s seconds ---" % (time.clock() - startTime))
    
