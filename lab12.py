
# CODE1: Perform Complex Arithmetic
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return f"{real_part} + i{imaginary_part}"

    def subtract(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return f"{real_part} + i{imaginary_part}"

complex1 = Complex(1, 2)
complex2 = Complex(2, 3)
print(complex1.add(complex2))
print(complex1.subtract(complex2))

# CODE2: Matrix Operations - Addition, Multiplication, Transpose
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]
        return result

    def multiply(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(3)] for i in range(3)]
        return result

matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix2 = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
print(matrix1.add(matrix2))
print(matrix1.multiply(matrix2))
print(matrix2.transpose())

# CODE3: Surface Area and Volume
class Shape:
    def get_choice(self):
        return int(input("PRESS 1 FOR CUBE, 2 FOR RECTANGULAR PRISM, 3 FOR SPHERE: "))

    def calculate_surface_area_and_volume(self, choice):
        if choice == 1:
            side = float(input("Enter the length of the side: "))
            print(f"Surface Area: {6 * side**2}, Volume: {side**3}")
        elif choice == 2:
            length = float(input("Enter the length: "))
            breadth = float(input("Enter the breadth: "))
            height = float(input("Enter the height: "))
            print(f"Surface Area: {2 * (length * breadth + breadth * height + height * length)}, Volume: {length * breadth * height}")
        elif choice == 3:
            radius = float(input("Enter the radius: "))
            print(f"Surface Area: {4 * 3.14159 * radius**2}, Volume: {(4 / 3) * 3.14159 * radius**3}")

shape = Shape()
shape.calculate_surface_area_and_volume(shape.get_choice())

# CODE4: Circumference Calculation
class Circumference:
    def get_choice(self):
        return int(input("PRESS 1 FOR SQUARE, 2 FOR RECTANGLE, 3 FOR CIRCLE: "))

    def calculate_circumference(self, choice):
        if choice == 1:
            side = float(input("Enter the length of the side: "))
            print(f"Circumference: {4 * side}")
        elif choice == 2:
            length = float(input("Enter the length: "))
            breadth = float(input("Enter the breadth: "))
            print(f"Circumference: {2 * (length + breadth)}")
        elif choice == 3:
            radius = float(input("Enter the radius: "))
            print(f"Circumference: {2 * 3.14159 * radius}")

circumference = Circumference()
circumference.calculate_circumference(circumference.get_choice())

# CODE5: Time Arithmetic
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def to_minutes(self):
        return f"{self.hours * 60 + self.minutes} minutes"

    def time_difference(self, other):
        hours_diff = abs(self.hours - other.hours)
        minutes_diff = abs(self.minutes - other.minutes)
        return f"{hours_diff} hours {minutes_diff} minutes"

    def to_12_hour_format(self):
        period = "AM"
        hours = self.hours
        if hours >= 12:
            period = "PM"
            if hours > 12:
                hours -= 12
        return f"{hours}:{self.minutes:02d} {period}"

time1 = Time(int(input("Enter hour (24-hour format) for Time 1: ")), int(input("Enter minutes for Time 1: ")))
time2 = Time(int(input("Enter hour (24-hour format) for Time 2: ")), int(input("Enter minutes for Time 2: ")))
print("Time 1 in minutes:", time1.to_minutes())
print("Time 2 in minutes:", time2.to_minutes())
print("Time difference:", time1.time_difference(time2))
print("Time 1 in 12-hour format:", time1.to_12_hour_format())
print("Time 2 in 12-hour format:", time2.to_12_hour_format())

# CODE6: Date Comparison
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

date1 = Date(13, 12, 2025)
date2 = Date(8, 7, 1458)
print(date1 == date2)

# CODE7: Weather Parameters
class Weather:
    def __init__(self, temperature, wind):
        self.parameters = [temperature, wind]

    def __contains__(self, item):
        return item in self.parameters

weather = Weather(25, True)
print(25 in weather)

# CODE8: String Operations
class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        else:
            self.value += str(other)
        return self

    def to_lower(self):
        self.value = self.value.lower()
        return self.value

    def to_upper(self):
        self.value = self.value.upper()
        return self.value

string1 = String("cAt")
print(string1.to_upper())
string2 = String(" and Dog")
string1 += string2
print("Concatenated String:", string1.value)
print("Lowercase String:", string1.to_lower())
print("Uppercase String:", string1.to_upper())