import time, itertools
startTime = time.clock()
maximum = 9999
#combinations = [i for i in itertools.permutations("abc")]
def generate(formula):
    n = 0
    while eval(formula) < 9999:
        yield eval(formula)
        n += 1
        
triangle = [i for i in generate("n * (n + 1) / 2") if i > 999]
square = [i for i in generate("n ** 2") if i > 999]
pentagonal = [i for i in generate("n * (3 * n - 1) / 2") if i > 999]
hexagonal = [i for i in generate("n * (2 * n - 1)") if i > 999]
heptagonal = [i for i in generate("n * (5 * n - 3) / 2") if i > 999]
octagonal = [i for i in generate("n * (3 * n - 2)") if i > 999]
ngon = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
def check(num1, num2): #checks if a number is in the form --ab, ab--
    if num1 % 100 == num2 // 100:
        return True
    return False

for a in itertools.permutations(ngon):
    for b in a[0]:
        for c in a[1]:
            if check(b, c):
                for d in a[2]:
                    if check(c, d):
                        for e in a[3]:
                            if check(d, e):
                                for f in a[4]:
                                    if check(e, f):
                                        for g in a[5]:
                                            if check(f, g) and check(g, b):
                                                print sum([b, c, d, e, f, g])

print("--- %s seconds ---" % (time.clock() - startTime))
