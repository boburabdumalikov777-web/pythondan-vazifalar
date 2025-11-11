"""Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
Notes"""
def find_odd(lst):
    for x in lst:
        if lst.count(x) % 2 != 0:
            return x
print(find_odd([5,5,5,2,1,4,2,1,4]))