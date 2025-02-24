# 
# Prompt the user to enter a string
user_input = input("Enter the string: ")

# Convert the string into a list of characters
char_list = list(user_input)

# Initialize an empty dictionary to store character frequencies
char_frequency = {}

# Outer loop to iterate over each character in the list
for i in range(len(char_list)):
    # Skip if the character is already processed
    if char_list[i] is None:
        continue
    # Initialize count for the current character
    count = 1
    # Inner loop to compare with subsequent characters
    for j in range(i + 1, len(char_list)):
        if char_list[i] == char_list[j]:
            count += 1
            # Mark the character as processed
            char_list[j] = None
    # Store the character and its frequency in the dictionary
    char_frequency[char_list[i]] = count

# Display the character frequencies
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
