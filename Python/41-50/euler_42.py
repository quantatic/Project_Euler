import time
total = 0
startTime= time.clock()
f = open('C:\Users\Aidan\Desktop\words.txt', 'r')
array = [sum([ord(j) - 64 for j in list(i)]) for i in f.read().replace("\"", "").split(",")] #got damn, that's complex
triangular = [(n * (n + 1)) / 2 for n in range(19)]
for i in array:
    if i in triangular:
        total += 1

print("--- %s triangular words ---" % total)
print("--- %s seconds ---" % (time.clock() - startTime))
