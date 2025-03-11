n=int(input("Enter the end value: "))
l1=[]
def compute(n):
    for i in range(1,n+1):
        l1.append(n**i)
    t1=tuple(l1)
    print(t1)
compute(n)
        

