str=input("enter your string:")
d=dict()
count=0

for i in str:
    if i not in d:
        
        d.update({i:count})
    if i in d:
        d[i]=d[i]+1
        
    
        
        

        

print(d)