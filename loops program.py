import math

def print_alphabets():
    print("Uppercase Alphabets:", "".join(chr(i) for i in range(65, 91)))
    print("Lowercase Alphabets:", "".join(chr(i) for i in range(97, 123)))

def multiplication_table(n):
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def count_alphabets_digits(s):
    alphabets = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    print(f"Alphabets: {alphabets}, Digits: {digits}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n**2).endswith(str(n))

def check_number_properties(n):
    print(f"Number {n} Properties:")
    print(f"Prime: {is_prime(n)}")
    print(f"Perfect: {is_perfect(n)}")
    print(f"Armstrong: {is_armstrong(n)}")
    print(f"Palindrome: {is_palindrome(n)}")
    print(f"Automorphic: {is_automorphic(n)}")

def generate_pythagorean_triplets():
    print("Pythagorean Triplets with side length <= 30:")
    for a in range(1, 31):
        for b in range(a, 31):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and c <= 30:
                print(f"({a}, {b}, {int(c)})")

def print_24_hour_format():
    for hour in range(24):
        if hour == 0:
            print("12 Midnight")
        elif hour < 12:
            print(f"{hour} AM")
        elif hour == 12:
            print("12 Noon")
        else:
            print(f"{hour - 12} PM")

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

def print_combinations_permutations(n, r):
    print(f"nCr ({n}C{r}): {nCr(n, r)}")
    print(f"nPr ({n}P{r}): {nPr(n, r)}")

def print_n_natural_reverse(n):
    print("Natural Numbers in Reverse:", list(range(n, 0, -1)))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def sin_x(x_rad):
    sin_value = 0
    for i in range(10):
        term = ((-1) ** i) * (x_rad ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_value += term
    return sin_value

def main():
    print_alphabets()
    multiplication_table(5)
    count_alphabets_digits("Hello123")
    check_number_properties(28)
    generate_pythagorean_triplets()
    print_24_hour_format()
    print_combinations_permutations(5, 3)
    print_n_natural_reverse(10)
    fibonacci(10)
    x_degrees = 30
    x_radians = x_degrees * math.pi / 180
    print(f"sin({x_degrees}°) ≈ {sin_x(x_radians)}")

if __name__ == "__main__":
    main()
