#Faylni satr bo'yicha o'qish uchun Python dasturini yozing, uni massivda saqlang.
def massivga(filename):
    a=[]
    with open(filename) as x:
        for y in x:
            a.append(y)
        return a
print(massivga("bobur.txt"))