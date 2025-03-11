word=input("Enter a word: ")
def pallindrome(word):
    if word==word[::-1]:
        print("The word is pallindrome.")
    else:
        print("The word is not pallindrome.")
pallindrome(word)