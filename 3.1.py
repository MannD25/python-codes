user=str(input("enter your string "))
count=0
for i in range(0,len(user)):
    if user[i]=="a" or user[i]=="e" or user[i]=="i" or user[i]=="o" or user[i]=="u":
        count+=1
print(count)


