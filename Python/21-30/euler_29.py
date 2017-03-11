import time
firstTime = time.clock()
array = []
for i in range(2, 101):
    for j in range(2, 101):
        array.append(i ** j)
array = list(set(array))
print len(array)
print("--- %s seconds ---" % (time.clock() - firstTime))
