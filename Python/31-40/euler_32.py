import itertools, time
startTime = time.clock()
total = []
combo = itertools.permutations("123456789")
pan = [''.join(i) for i in combo]
pan = set(pan)
def checkPan(n):
    if n in pan:
        return True
    else:
        return False
print checkPan(123456789)
print checkPan(1234)
print checkPan(12345676789)
for i in range(1, 9999):
    for j in range(i, 9999):
        tempString = str(i) + str(j) + str(i * j)
        if len(tempString) > 9:
            break;
        if checkPan(tempString) and i * j not in total:
            total.append(i * j)
            print("i", i, "j", j, "product", i * j)
print("--- sum of pandigitals is: %s ---" % sum(total))
print("--- %s seconds ---" % (time.clock() - startTime))
