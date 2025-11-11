"""Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

Return a boolean value (True or False).
Return True if the amount of x's and o's are the same.
Return False if they aren't the same amount.
The string can contain any character.
When "x" and "o" are not in the string, return True.
Examples
XO("ooxx") ➞ True

XO("xooxx") ➞ False

XO("ooxXm") ➞ True
# Case insensitive.

XO("zpzpzpp") ➞ True
# Returns True if no x and o.

XO("zzoo") ➞ False"""
def XO(txt):
    a="xX"
    b="oO"
    z=""
    y=""
    for x in txt:
        if x in a:
            z+=x
    for x in txt:
        if x in b:
            y+=x
    return len(z)==len(y)
print(XO("bobur"))
print(XO("xusanbOy"))