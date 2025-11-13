def filt(lst):
    a=[]
    for x in lst:
        if x%2==0:
            a.append(x)
    return a
print(filt([1,2,3,4,5,6]))
print(filt([]))