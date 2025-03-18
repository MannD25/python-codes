def count(lst):
    if len(lst)==0:
        return 0
    else:
        return 1 + count(lst[1:])
    return count 
lst=[1,2,3,4,5,6,7]
print(count(lst))