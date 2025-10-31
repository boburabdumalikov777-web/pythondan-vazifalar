'''Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4'''
def count_vowels(txt):
    unlilar="aueoiAUEOI"
    yigindi=0
    for x in txt:
	    if x in unlilar :
		    yigindi +=1
    return yigindi
print(count_vowels("bObur"))
print(count_vowels("Mustafo"))