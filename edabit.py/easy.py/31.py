"""Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"""
def replace_vowels(txt,ch):
    x="aeuioAEUOI"
    y=""
    for i in txt:
        if i in x:
            y+=ch
        else:
            y+=i
    return y
print(replace_vowels("bobur","?"))