#Matnli faylni o'qiydigan, ma'lum bir so'zning barcha ko'rinishlarini boshqa
#  so'z bilan almashtiradigan va o'zgartirilgan tarkibni yangi faylga yozadigan dastur yozing.
def alishtir(filename,newfile,soz,newsoz):
    with open(filename,"r") as x:
        y=x.read()
    z=y.replace(soz,newsoz)
    with open(newfile,"w") as x:
        z=x.write(z)
    with open(newfile,"r") as x:
        s=x.read()
    return s
print(alishtir("bobur.txt","yangi1.txt","2003","2001"))