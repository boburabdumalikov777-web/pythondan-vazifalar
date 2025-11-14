#Matn faylidagi qatorlar sonini hisoblash uchun Python dasturini yozing.
def satr(filename):
    a=[]
    with open(filename,"r") as x:
        for y in x:
            a.append(y)
        l=len(a)
        return l
print(satr("bobur.txt"))