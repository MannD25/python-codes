b=int(input("enter your year"))
if b%4==0 or b%100==0 or b%400==0:
    print("leap year")
else:
    print("not a leap year ")