'''Write two functions:

to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.
Examples
to_int("77") ➞ 77

to_int("532") ➞ 532

to_str(77) ➞ "77"

to_str(532) ➞ "532"'''
def to_int(txt):
	return int(txt)

def to_str(num):
	return str(num)
print(to_int("45"))
print(to_str(36))