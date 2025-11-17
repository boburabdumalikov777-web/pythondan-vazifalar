#Birinchi fayldagi har bir satrni ikkinchi fayldagi tegishli qator bilan birlashtirish uchun Python dasturini yozing.
def qosh(file1,file2):
    with open(file1) as x, open(file2) as f:
        for y,z in zip(x,f):
            with open("cd.txt","a") as b:
                q=b.write(y+z)
    with open("cd.txt") as b:
        s=b.read()
    return s
print(qosh("bobur.txt","sardor.txt"))