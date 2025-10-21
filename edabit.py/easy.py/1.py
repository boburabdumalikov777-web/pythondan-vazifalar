'''Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

Alternative Text

Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25'''
def dis(price, discount):
	return round(price-discount*price/100, 2)
print(dis(1500, 50)) #➞ 750
print(dis(89, 20))#➞ 71.2
print(dis(999,22))
