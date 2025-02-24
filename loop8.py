def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n

N=int(input("enter n "))
r=int(input("enter r "))
result=fact(N)/(fact(N-r)*fact(r))
print(result)