"""There's a great war between the even and odd numbers. Many numbers already lost their lives in this war and it's your task to end this. You have to determine which group sums larger: the evens or the odds. The larger group wins.

Create a function that takes a list of integers, sums the even and odd numbers separately, then returns the difference between the sums of the even and odd numbers.

Examples
war_of_numbers([2, 8, 7, 5]) ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 is larger than 10
# So we return 12 - 10 = 2

war_of_numbers([12, 90, 75]) ➞ 27

war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168"""
def war_of_numbers(lst):
    a=0
    b=0
    for x in lst:
        if x%2==0:
            a+=x
        else:
            b+=x
    if a>b:
        c=a-b
    else:
        c=b-a
    return c
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
print(war_of_numbers([12, 90, 75]))
print(war_of_numbers([2, 8, 7, 5]))