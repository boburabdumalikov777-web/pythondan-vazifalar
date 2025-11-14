#Faylga matn qo'shish va matnni ko'rsatish uchun Python dasturini yozing.
def filegaqosh(filename):
    from itertools import islice  #buni import qilish kerakligini tushundim
    with open(filename,"a") as x:
        x.write("\nhozirda olmaliqda yashayabman")
    with open(filename) as y:
        b=y.read()
    return b
print(filegaqosh("bobur.txt"))