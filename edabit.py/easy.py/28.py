'''Create a function that takes a string and replaces the vowels with another character.

a = 1
e = 2
i = 3
o = 4
u = 5
Examples
replace_vowel("karachi") ➞ "k1r1ch3"'''
def replace_vowel(word):
    lugat={"a":"1","e":"2","i":"3","o":"4","u":"5"}
    x=""
    for y in word:
        if y in lugat:
            x+=lugat[y]
        else:
            x+=y
    return x
print(replace_vowel("bobur"))