# Eng uzun so'zlarni topish uchun python dasturini yozing.
def uzun(filename):
    uzunstring = ""
    enguzun = 0
    with open(filename,"r") as x:
        for y in x:
            b = y.split(",")
            for d in b:
                if len(d) > enguzun:
                    enguzun = len(d)
                    uzunstring = d
    return uzunstring
print(uzun("bobur.txt"))
