def average(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+average(lst[1:])
    
lst=[1,-3,3,4,5]
print(average(lst)/len(lst))