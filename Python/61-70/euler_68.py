import time, itertools
array = [i for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
for i in array:
    tmp = [[i[0], i[1], i[2]], [i[3], i[2], i[4]], [i[5], i[4], i[6]], [i[7], i[6], i[8]], [i[9], i[8], i[1]]]
    
