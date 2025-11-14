#Faylni satr bo'yicha o'qish va uni ro'yxatga saqlash uchun Python dasturini yozing.
def dlyalist(filename):
    a=[]
    with open(filename) as x:
        for y in x:
            a.append(y)
        return a
print(dlyalist("bobur.txt"))