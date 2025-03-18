def pow(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)
a=int(input("Enter a positive integer: "))
b=int(input("Enter a positive integer: "))
print(pow(a,b))
