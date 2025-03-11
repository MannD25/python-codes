word=input("enter your string")
def convert(word):
    w1=set(word)
    w2=list(w1)
    w3=[]
    w4=[]
    for i in w2:
        if i==' ':
            w2.remove(i)
    for i in w2:
        if i.isalpha():
            w3.append(i)
        else:   
            w4.append(i)
    w3.sort()
    w4.sort()
    w5=w3+w4
    print(w5)
print(convert(word))