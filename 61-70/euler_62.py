import time, itertools
startTime = time.clock()
i = 0
minimum = 10 ** 50
cubes = {}
while True:
    tmp = "".join(sorted(str(i ** 3)))
    if tmp in cubes:
        cubes[tmp][0]+= 1
        if cubes[tmp][0] == 5:
            minimum = min(cubes[tmp][1], minimum)
    else:
        cubes[tmp] = [1, i]
    i += 1
    if len(str(i ** 3)) > len(str(minimum)):
        print minimum ** 3
        break
print("--- %s seconds ---" % (time.clock() - startTime))
