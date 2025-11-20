#Fayldan yangi qator belgilarini olib tashlash uchun Python dasturini yozing.
def yangi(filename,newfile):
    a=[]
    with open(filename,"r") as x:
        for y in x:
            a.append(y)
    b=a.pop(-1)
    with open(newfile,"w") as x:
        for y in a:
            c=x.write(y)
    with open(newfile,"r") as x:
        r=x.read()
    return r
print(yangi("bobur.txt","yangi.txt"))