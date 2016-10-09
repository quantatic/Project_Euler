biggest = 0
def collatz(input):
    seq = [input]
    while input > 1:
        if input % 2 == 0:
            input = input / 2
        else:
            input = (input * 3) + 1
        seq.append(input)
    return seq

for i in range(1, 1000001):
    if len(collatz(i)) > len(collatz(biggest)):
        biggest = i
        print(i)
print biggest
    
