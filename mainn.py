a=int(input("enter your number "))
b=3
#1
print(a+b)
#2
print(b-a)
#3
print(b*a)
#4
print(b/a)

#6
hours=int(input("enter the hours"))
print("minutes =" ,hours*60)
#7
minutes=int(input("enter minutes"))
print("hours=",minutes/60)
#8
dollar=int(input("enter dollar"))
print("rupees =",dollar*48)
#9
rupees=int(input("enter rupees"))
print("dollar=",rupees/48)
#10
dollar=int(input("enter dollar"))
pound=(dollar*70)/48
print("pound is ",pound)
#11
grams=int(input("enter the grams"))
print("kg is ",grams/1000)
#12
ks=int(input("enter the kgrams"))
print("grams is ",ks*1000)
#13
bytes=int(input("enter bytes"))
kb=bytes/1024
mb=kb/1024
gb=mb/1024
print("kb is ",kb,"gb is ",gb,"mb is ",mb)
# 1. Convert bytes into KB, MB, and GB
def convert_bytes(bytes):
    KB = bytes / 1024
    MB = KB / 1024
    GB = MB / 1024
    return KB, MB, GB

# 2. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(C):
    F = (9 / 5 * C) + 32
    return F

# 3. Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(F):
    C = 5 / 9 * (F - 32)
    return C

# 4. Calculate interest
def calculate_interest(P, R, N):
    I = (P * R * N) / 100
    return I

# 5. Calculate area and perimeter of a square
def square_properties(L):
    area = L ** 2
    perimeter = 4 * L
    return area, perimeter

# 6. Calculate area and perimeter of a rectangle
def rectangle_properties(L, B):
    area = L * B
    perimeter = 2 * (L + B)
    return area, perimeter

# 7. Calculate area of a circle
def circle_area(R):
    area = (22 / 7) * R ** 2
    return area

# 8. Calculate area of a triangle
def triangle_area(H, L):
    area = (H * L) / 2
    return area

# 9. Calculate net salary
def net_salary(gross_salary):
    allowance = 0.10 * gross_salary
    deduction = 0.03 * gross_salary
    net_salary = gross_salary + allowance - deduction
    return net_salary

# 10. Calculate net sales
def net_sales(gross_sales):
    discount = 0.10 * gross_sales
    net_sales = gross_sales - discount
    return net_sales

# Testing the functions
if __name__ == "__main__":
    # Example inputs
    bytes = 1048576
    C = 25
    F = 77
    P, R, N = 10000, 5, 2
    L = 5
    B = 10
    R_circle = 7
    H, L_triangle = 10, 5
    gross_salary = 50000
    gross_sales = 100000

    # Results
    print("Bytes to KB, MB, GB:", convert_bytes(bytes))
    print("Celsius to Fahrenheit:", celsius_to_fahrenheit(C))
    print("Fahrenheit to Celsius:", fahrenheit_to_celsius(F))
    print("Interest:", calculate_interest(P, R, N))
    print("Square (Area, Perimeter):", square_properties(L))
    print("Rectangle (Area, Perimeter):", rectangle_properties(L, B))
    print("Circle Area:", circle_area(R_circle))
    print("Triangle Area:", triangle_area(H, L_triangle))
    print("Net Salary:", net_salary(gross_salary))
    print("Net Sales:", net_sales(gross_sales))
#24
a=int(input("enter a "))
b=int(input("enter b"))
c=a
a=b
b=c
print("a now is ",a,"b now is ",b)




