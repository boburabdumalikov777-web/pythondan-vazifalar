# Fayldan tasodifiy qatorni o'qish uchun Python dasturini yozing.
def tas(filename):
    import random
    a=[]
    with open(filename,"r") as x:
        for y in x:
            a.append(y)
    b=random.choice(a)
    return  b
print(tas("bobur.txt"))