<<<<<<< HEAD
str=input("enter your string:")
d=dict()
count=0

for i in str:
    if i not in d:
        
        d.update({i:count})
    if i in d:
        d[i]=d[i]+1
        
    
        
        

        

print(d)
=======

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
>>>>>>> 9788cd2c4ad663a52592b6fabb96a7e22157bf59
