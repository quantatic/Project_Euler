import itertools, time
startTime = time.clock()
array = [i for i in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
array.sort()
print array[999999]
print "--- %s seconds ---" % (time.clock() - startTime)
