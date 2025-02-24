user=input("enter a string ")
countalpha=0
countnum=0
for i in user:
    if i.isalpha()==True:
        countalpha+=1
        
    else:
        countnum+=1
print(countnum,"are numbers  ",countalpha,"are alphabets")