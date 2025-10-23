'''Create a function that evaluates an equation.

Examples
eq("1+2") ➞ 3

eq("6/(9-7)") ➞ 3

eq("3+2-4") ➞ 1'''
import math
def eq(evaluate):
	return eval(evaluate)
print(eq("3+2-4"))
print(eq("6/(9-7)"))