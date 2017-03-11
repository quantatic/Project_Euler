import time
startTime = time.clock()
total = 0
def isPalin(num):
    if not str(num) == str(num)[::-1]: #if not a palindrome
        return False
    else: #if is a palindrome
        return True

for i in range(1, 1000000, 2):
    if isPalin(i) and isPalin(bin(i)[2:]):
        total += i

print("---total of all palindromes: %s" % total)
print("--- %s seconds ---" % (time.clock() - startTime))
raw_input("Press enter to exit")
