"""An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

Examples
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False"""
def is_isogram(txt):
    a=txt.lower()
    return len(a)==len(set(a))
print(is_isogram("Algorism"))
print(is_isogram("PasSword"))