import time
total = 0
startTime = time.clock()
def check(num):
    for j in range(50):
        num += int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            return False
    return True

for i in range(10000):
    if check(i):
        total += 1
        
print total
print("--- %s seconds ---" % (time.clock() - startTime))

