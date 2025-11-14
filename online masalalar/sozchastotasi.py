# Fayldagi so'zlarning chastotasini hisoblash uchun Python dasturini yozing.
from collections import Counter
import re


def chastota(filename):
    with open(filename, "r") as x:
        a = x.read()
        b = re.findall(r"\b\w+\b", a)
        sanoq = Counter(b)
    return sanoq


print(chastota("bobur.txt"))
# re — bu regular expressions (regulyar ifodalar) modulidir.
# Matnda qidirish, tekshirish, ajratish, almashtirish kabi operatsiyalarni bajarish uchun ishlatiladi.
#collections — bu Python standart kutubxonasidagi modul bo‘lib, ma’lumot tuzilmalari bilan ishlashga yordam beradi.

#Counter esa collections modulidagi maxsus obyekt bo‘lib, u elementlar chastotasini hisoblash uchun ishlatiladi.