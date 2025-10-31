'''Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9'''
def is_triplet(n1, n2, n3):
	if n1<n3 and n2<n3:
		return n3**2==n2**2+n1**2
	elif n1<n2 and n3<n2:
		return n2**2==n1**2+n3**2
	elif n2<n1 and n3<n1:
		return n1**2==n2**2+n3**2
print(is_triplet(5,4,3))
print(is_triplet(7,2,9))