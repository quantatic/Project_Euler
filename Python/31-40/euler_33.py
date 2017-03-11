import time
startTime = time.clock()
totalD = 1
totalN = 1
for n in range(10, 100):
    for d in range(10, 100):
        n = float(n)
        d = float(d)
        if n % 10 == 0 or d % 10 == 0 or n / d >= 1:
            continue
        Ln, Ld = [n // 10, n % 10], [d // 10, d % 10]
        if any(i in Ln for i in Ld) and not all(i in Ln for i in Ld):
            if Ld[0] in Ln:
                x = Ld[0] #x is the number which we're going to remove
            else:
                x = Ld[1]
            Ln.remove(x)
            Ld.remove(x)
           # print(Ln, Ld, n, d)
            if n / d == Ln[0] / Ld[0]:
                totalD = totalD * Ld[0]
                totalN = totalN * Ln[0]

print totalN / totalD


print("--- %s seconds ---" % (time.clock() - startTime))
