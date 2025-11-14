#Faylning oxirgi n qatorini o'qish uchun Python dasturini yozing.
def oqish(filename,line):
    a=[]
    with open(filename) as x:
        for y in x:
            a.append(y)
    f=a[-line:]
    return f
print(oqish("bobur.txt",2))