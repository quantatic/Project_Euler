import time
startTime = time.clock()
maxCycle = 0
maxDenom = 0
def calcFraction(num): #calculates 1/num
    total = "0."
    remainder = 1
    for i in range(10):
        if num == 0:
            break
        remainder *= 10
        if not remainder % num == remainder:
            total += str(remainder / num)
            remainder = remainder % num
        else:
            total += "0"

def calcRemainder(num): #calculates 1/num
    remainders = [10]
    for i in range(10000): #set a realistic cap, we're breaking out of this anyways
        if (remainders[-1] % num) * 10 not in remainders: #if we haven't already calculated our current remainder
            if not remainders[-1] % num == remainders[-1]: #if we can divide our current number into our remainder
                remainders.append(remainders[-1] % num)
            else:
                remainders.append(remainders[-1] * 10)
        else:
            return remainders #if we've already found this, return it
    
for i in range(1, 1000):
    if len(calcRemainder(i)) > maxCycle:
        maxCycle = len(calcRemainder(i))
        maxDenom = i

print("--- 1/%s gives the maximum size cycle ---" % maxDenom)
print("--- %s seconds ---" % (time.clock() - startTime))
