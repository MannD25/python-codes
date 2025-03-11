def count_lower_upper(s):
    result = {"upper": 0, "lower": 0}
    for char in s:
        if char.isupper():
            result["upper"] += 1
        elif char.islower():
            result["lower"] += 1
    return result

input_string = "Hello World!"
counts = count_lower_upper(input_string)
print(counts)  # Output: {'upper': 2, 'lower': 8}