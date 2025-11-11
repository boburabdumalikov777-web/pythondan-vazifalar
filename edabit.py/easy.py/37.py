"""Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]"""
def filter_list(lst):
	a=[]
	for x in lst:
		if isinstance(x,int):
			a.append(x)
	return a
print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))