# Fayl mazmunini boshqa faylga nusxalash uchun Python dasturini yozing.
def nusxsa(filename, newfile):
    a = []
    with open(filename) as l:
        for y in l:
            b = a.append(y)
    with open(newfile, "a") as x:
        for y in a:
            z = x.write(y)
    with open(newfile, "r") as g:
        h = g.read()
    return h


print(nusxsa("bobur.txt", "sardor.txt"))
