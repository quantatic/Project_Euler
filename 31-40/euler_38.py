import time, itertools
startTime = time.clock()
maxPan = 0
pans = list(["".join(i) for i in itertools.permutations("123456789")])
def checkPan(num):
    tmp = ""
    for i in range(1, 10):
       tmp += str(i * num)
       if len(str(tmp)) >= 9:
           break
    if tmp in pans:
        return True
    else:
        return False
    
for i in xrange(10000):
    if checkPan(i):
            print i

            
print("--- max pandigital multiple is %s " % maxPan)
print("--- %s seconds ---" % (time.clock() - startTime))
