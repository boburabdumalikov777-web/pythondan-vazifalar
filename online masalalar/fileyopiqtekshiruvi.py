# Fayl yopilgan yoki yopilmaganligini baholash uchun Python dasturini yozing.
def holat(filename):
    if filename.closed:
        return "file yopiq"
    else:
        return "file hali ochiq"
f=open("bobur.txt")
f.close()
print(holat(f))