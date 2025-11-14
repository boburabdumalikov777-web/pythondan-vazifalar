def fayloqi(filename):
    with open(filename) as x:
        a = x.readline()
    return a
print(fayloqi("bobur.txt"))