#Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

def frequency(s):
    words = s.split()
    return {word: words.count(word) for word in sorted(set(words))}

print(frequency("the quick brown fox jumps over the lazy dog")) 