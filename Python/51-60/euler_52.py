import time
startTime = time.clock()
z = 1
def checkNumber(num): #this way works too, but using sorted returns an answer faster
    for i in range(1, 7):
        if not all([j in str(num) for j in str(i * num)]):
            return False
    return True

while True:
    #if checkNumber(z):
    if sorted(str(z)) == sorted(str(z * 2)) == sorted(str(z * 3)) == sorted(str(z * 4)) == sorted(str(z * 5)) == sorted(str(z * 6)):
        break
    z += 1

print z
print ("--- %s seconds ---" % (time.clock() - startTime))
