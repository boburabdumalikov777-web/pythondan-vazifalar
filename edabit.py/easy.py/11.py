'''Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4'''
def calculator(num1, operator, num2):
	if operator=="+":
		return num1+num2
	elif operator=="-":
		return num1-num2
	elif operator=="*":
		return num1*num2
	elif operator=="/":
		if num2 !=0:
			return num1/num2
		else:
			return "Can't divide by 0!"
	else:
		return "notogri operator"
print(calculator(4,"+",8))
print(calculator(8,"/",0))