import time, itertools
startTime = time.clock()
array = ["".join(i) for i in itertools.permutations("0123456789")]
divisors = [2, 3, 5, 7, 11, 13, 17]
total = 0

def testNumber(num):
    for j in range(len(divisors)):
        if not int(num[j + 1] + num[j + 2] + num[j + 3]) % divisors[j] == 0:
            return False
    return True

for i in array:
    if testNumber(i):
        total += int(i)
        
print("--- your answer is %s ---" % total)
print("--- %s seconds ---" % (time.clock() - startTime))
