'''ate a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4'''

def count_vowels(txt):
    x="aueoiAUEOI"
    z=[]
    for y in txt:
        if y in x:
            z.append(y)
    return len(z)
print(count_vowels("bobur"))