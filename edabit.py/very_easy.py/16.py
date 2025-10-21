'''You call your spouse in anger and a "little" argument takes place. Count the total amount of insults used. Given a dictionary of insults, return the total amount of insults used.

Example
total_amount_adjectives({ "a": "moron" }) ➞ 1

total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ➞ 3

total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", d: "dirtbag" }) ➞ 4'''
def total_amount_adjectives(dct):
	return len(dct)
print(total_amount_adjectives({"a":"svolch","b":"suka"}))