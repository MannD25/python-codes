
user_input = input("Enter the string: ")

char_list = list(user_input)

char_frequency = {}

for i in range(len(char_list)):
    if char_list[i] is None:
        continue
    count = 1
    for j in range(i + 1, len(char_list)):
        if char_list[i] == char_list[j]:
            count += 1
            char_list[j] = None
    char_frequency[char_list[i]] = count

print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
