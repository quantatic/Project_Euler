import itertools, time
startTime = time.clock()
f = open('C:\Users\Aidan\Desktop\p059_cipher.txt', 'r')
code = [int(i) for i in f.read().split(",")]
words = range(32, 123)

def isValid(key):
    for j in range(len(code)):
        if not code[j] ^ key[j % 3] in words:
            return False
    return True

for a in words:
    for b in words:
        for c in words:
            i = [a, b, c]
            if isValid(i):
                tmp = ""
                for j in range(len(code)):
                    tmp += chr(code[j] ^ i[j % 3])
                print tmp, sum(ord(_) for _ in tmp)
print("--- %s seconds ---" % (time.clock() - startTime))


    

