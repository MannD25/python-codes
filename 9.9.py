s1=input("enter your string ")
def count_alpha_digits(s1):
    result={"alpha":0,"digits":0}
    for char in s1:
        if char.isalpha():
            result["alpha"]+=1
        elif char.isdigit():
            result["digits"]+=1
    return result
print(count_alpha_digits(s1))