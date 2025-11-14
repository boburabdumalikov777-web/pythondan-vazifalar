# Faylga ro'yxat yozish uchun Python dasturini yozing.
def roy(filename,lst):
    for x in lst:
        with open(filename,"a") as y:
            z=y.write(x)
    with open(filename,"r") as c:
        s=c.read()
    return s
print(roy("bobur.txt",["bobur","sardor"]))