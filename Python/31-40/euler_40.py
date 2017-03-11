import time
startTime= time.clock()
frac = ""
total = 1
counter = 1
while len(frac) < 1000001:
    frac += str(counter)
    counter += 1
print("--- The answer is %s ---" % (int(frac[0]) * int(frac[9]) * int(frac[99]) * int(frac[999]) * int(frac[9999]) * int(frac[99999]) * int(frac[999999])))
print("--- %s seconds ---" % (time.clock() - startTime))
