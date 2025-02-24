user = input("Enter a string: ")
result = ""

for char in user:
    if 'a' <= char <= 'z':  # Check if character is lowercase
        result += chr(ord(char) - 32)  # Convert to uppercase
    else:
        result += char  # Keep other characters unchanged

print(result)
