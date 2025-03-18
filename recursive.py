def prime_factors(n, i=2):
    if i * i > n:
        return [n] if n > 1 else []
    if n % i:
        return prime_factors(n, i + 1)
    return [i] + prime_factors(n // i, i)
n = int(input("Enter a positive integer: "))
print(prime_factors(n))
