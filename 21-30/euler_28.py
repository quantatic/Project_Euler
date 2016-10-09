import time
add = 1
addAdd = 2
startTime = time.clock()
total = 1
for i in range(500):
    for i in range(4):
        add = addAdd + add
        total = total + add
    addAdd = addAdd + 2
print total
print add
