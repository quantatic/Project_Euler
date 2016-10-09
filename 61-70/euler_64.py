import time
from math import sqrt
startTime = time.clock()
def continued(num):
    answer = []
    answer.append(int(sqrt(num)))
    answer.append(int(1 / (sqrt(num) - answer[-1])))
    
    print answer
continued(23)
#print test[:len(test) / 2] == test[len(test) / 2:]
