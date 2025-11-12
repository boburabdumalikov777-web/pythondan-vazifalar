"""Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

Examples
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]
Try to use list comprehensions in your solution. Here's an example:

vals = [expression 
  for value in collection 
    if condition]
This is equivalent to:

vals = []
for value in collection:
  if condition:
    vals.append(expression)"""
def find_even_nums(num):
    b=[]
    x=1
    while x<=num:
        if x%2==0:
            b.append(x)
        x+=1
    return b
print(find_even_nums(9))
print(find_even_nums(15))
print(find_even_nums(1))