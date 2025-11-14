def fayloqi(filename):
    with open(filename) as x:
        a = x.read()
    return a


#print(fayloqi(r"C:\Users\Computer7\.bobur\pythondan-vazifalar\online masalalar\bobur.txt"))  agar yurgizilayotgan file va oqilayotgan file bir joyda
#  joylashmagan bolasa shu holatda path korsatish kerak
print(fayloqi("bobur.txt"))