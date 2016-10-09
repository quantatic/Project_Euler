number = 1
for i in range(1, 101):
    number = number * i
print(sum([int(i) for i in list(str(number))]))
