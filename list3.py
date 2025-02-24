import random 
lst=[]
for i in range(50):
     i=random.randrange(1,30)
     lst.append(i)
print(lst)
lst2=[]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):  
        if lst[i] != lst[j] and lst[i] not in lst2:  
              lst2.append(lst[i])
              
print(lst2)
