"""Create a function that takes a string and returns a string with its letters in alphabetical order.

Examples
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"""
def alphabet_soup(txt):
    a=list(txt)
    b=sorted(a)
    c=""
    for x in b:
        c+=x
    return c
print(alphabet_soup("bad"))
print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))