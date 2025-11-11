"""The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr""" 
def reverse(txt):
	a=txt.swapcase()
	b=""
	for x in a:
		b=x+b
	return b
print(reverse("hello world"))
print(reverse("ReVeRsE"))