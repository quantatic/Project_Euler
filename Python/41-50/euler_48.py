import time
startTime = time.clock()
answer = 0
for i in range(1, 1001):
    answer += i ** i
print("--- your answer is: %s ---" % str(answer)[-10::])
print("--- %s seconds ---" % (time.clock() - startTime))
