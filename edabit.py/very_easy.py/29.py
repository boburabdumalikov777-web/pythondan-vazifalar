'''Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.

Examples
divisible_by_five(5) ➞ True

divisible_by_five(-55) ➞ True

divisible_by_five(37) ➞ False'''
def divisible_by_five(n):
	return n%5==0
print(divisible_by_five(45))
print(divisible_by_five(40))
print(divisible_by_five(22))