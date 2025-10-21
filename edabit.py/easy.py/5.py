'''Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.

Examples
number_split(4) ➞ [2, 2]

number_split(10) ➞ [5, 5]

number_split(11) ➞ [5, 6]

number_split(-9) ➞ [-5, -4]'''
def number_split(n):
	x=n//2
	y=n-x
	return ([x,y])
print(number_split(75))
print(number_split(14))