import time
startTime = time.clock()
total = 0
f = open("C:/Users/Aidan/Desktop/p022_names.txt")
array = f.read().replace("\"", "").split(",")
array.sort()
for i in range(len(array)):
    tmp = 0
    for j in list(array[i]):
        tmp = tmp + ord(j) - 64
    total = total + (tmp * (i + 1))
print total
print("--- %s seconds ---" % (time.clock() - startTime))
    
