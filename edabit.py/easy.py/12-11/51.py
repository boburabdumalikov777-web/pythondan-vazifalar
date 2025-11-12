"""Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Examples
probability([5, 1, 8, 9], 6) ➞ 50.0

probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7

probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0
Notes"""
def probability(lst, n):
    a=0
    for x in lst:
       if x>=n:
           a+=1 
    y=round(100*a/len(lst),1)
    return y
print(probability([5, 1, 8, 9], 6))
print(probability([7, 4, 17, 14, 12, 3], 16))
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))