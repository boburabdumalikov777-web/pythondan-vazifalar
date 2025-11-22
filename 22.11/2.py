#Return the Index of All Capital Letters
"""Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]"""
def index_of_caps(word):
    a=[]
    for x, y in enumerate(word):  # x indexni oladi, y sozdagi belgini
        if y.isupper():
            a.append(x)
    return a
print(index_of_caps("BobUr"))
print(index_of_caps("sARDoR"))