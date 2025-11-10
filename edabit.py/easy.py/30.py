'''Create a function that returns True if a given inequality expression is correct and False otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False'''
def correct_signs(txt):
	return eval(txt)
print(correct_signs("6>5>3>2<4"))