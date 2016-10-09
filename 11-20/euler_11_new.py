def makeInt(array): #turns an array of integers formatted as strings into ints
    tempArray = []
    for i in array:
        tempArray.append(int(i))
    return tempArray

#string of numbers, formatted just as project euler formats theirs
numberString = """1 25 13 16 13 15 95 15 98 02
14 64 61 12 67 14 85 12 96 12
98 89 23 49 65 51 96 48 13 06 12
15 95 14 54 14 58 32 95 12 05
98 14 53 09 13 00 00 14 64 12"""

numberArray = []

for i in numberString.split("\n"): #gets every single seperate line
    numberArray.append(makeInt(i.split(" "))) #splits each line at spaces

print numberArray


