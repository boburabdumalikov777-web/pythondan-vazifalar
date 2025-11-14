# Oddiy faylning fayl hajmini olish uchun Python dasturini yozing.
import os
def siz(filename):
    a = os.path.getsize(filename)
    return a
print(siz("bobur.txt"))
#os moduli nima?

#os moduli — Python standart kutubxonadagi modul bo‘lib, u sizga operatsion tizim bilan ishlash imkoniyatini beradi.

#masalan, fayl tizimi bilan ishlash, papkalar yaratish, fayllar hajmini olish, yo‘l (path) bilan ishlash va hokazo.