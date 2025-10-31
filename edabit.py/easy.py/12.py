'''Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.

Examples
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000'''
#Return "invalid" if damage or speed is negative.
def damage(damage, speed, time):
	if damage<0 or speed<0:
		return "invalid"
	if time=="second":
		seconds=1
	elif time=="minute":
		seconds=60
	elif time=="hour":
		seconds=3600
	else:
		return "invalid"
	return damage*speed*seconds
print(damage(40, 5, "second"))
print(damage(100,1,"minute"))