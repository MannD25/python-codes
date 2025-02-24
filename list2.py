import random 
lst=[]
for i in range(20) :
    i=random.randrange(1,100)
    lst.append(i)
user=int(input("enter a number "))
if user in lst:
    print("number present ")
else:
    print("number not present ")