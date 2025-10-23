'''Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.

Examples
makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True'''
def makes10(a, b):
	return a==10 or b==10 or a+b==10
print(makes10(5,5))
print(makes10(10,4))
print(makes10(8,7))