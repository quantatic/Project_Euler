from math import sqrt
import time
startTime = time.clock()
total = 0
def properDivisors(number):
    array = [1]
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            array.append(i)
            array.append(number / i)
    if(int(sqrt(number)) == sqrt(number) and sqrt(number) not in array): #if the number is a perfect square, and the array doesn't already contain it
        array.append(int(sqrt(number)))
    array.sort()
    return array
for j in range(1, 10001):
    if(sum(properDivisors(sum(properDivisors(j)))) == j and j != sum(properDivisors(j))):
        total = total + j
        print j
print total
print("--- %s seconds ---" % (time.clock() - startTime))
