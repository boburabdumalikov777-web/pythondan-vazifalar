#Faylni satr bo'yicha o'qish uchun Python dasturini yozing, uni o'zgaruvchiga saqlang
def linyaoqi(filename):
    with open(filename,"r") as x:
        a=x.readline()
    return a
print(linyaoqi("bobur.txt"))