total = -1
for i in range(999999):
    sum = 0
    for j in list(str(i)):
        sum = int(j) ** 5 + sum
    if sum == i:
        total = total + i
print total
        
