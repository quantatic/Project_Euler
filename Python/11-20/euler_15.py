def latticeGrid(size):
    array = [[1 for j in range(size + 1)] for i in range(size + 1)]
    for i in range(size - 1, -1, -1):
        for j in range(size - 1, -1, -1):
            array[i][j] = array[i + 1][j] + array[i][j + 1]
    return array

def printArray(tempArray):
    for i in tempArray:
        print(i)

array = latticeGrid(20)

printArray(array)
print(array[0][0])
