'''Create a function that takes a list of numbers. Return the largest number in the list.

Examples
findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001'''
def findLargestNum(nums):
	return max(nums)
print(findLargestNum([15, 45, -55, 63]))