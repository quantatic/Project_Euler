import time
startTime = time.clock()
def fact(num):
    total = 1
    for i in range(2, num + 1):
        total = total * i
    return total

for i in range(2540161):
    tempTotal = 0
    array = [int(j) for j in list(str(i))]
    for j in array:
        tempTotal = tempTotal + fact(j)
        if tempTotal > i:
            continue
        if tempTotal == i:
            print i
print("--- %s seconds ---" % (time.clock() - startTime))


