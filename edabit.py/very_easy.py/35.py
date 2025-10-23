'''Create a function that returns how many possible arrangements can come from a certain number of switches (on / off). In other words, for a given number of switches, how many different patterns of on and off can we have?

Examples
pos_com(1) ➞ 2

pos_com(3) ➞ 8

pos_com(10) ➞ 1024
Notes'''
def pos_com(num):
	return 2**num
print(pos_com(2))
print(pos_com(10))
