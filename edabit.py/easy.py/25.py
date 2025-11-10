def numbers_sum(lst):
    z=0
    x=[1,2,3,4,5,6,7,8,9,0]
    for y in lst:
        if y in x:
            z+=y
    return z
print(numbers_sum([1,2,3,4,"45",True,False,"2"]))
print(numbers_sum([True, False, "123", "75"]))# 0
