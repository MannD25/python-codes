s={"Abhi","Ahi","Abi","Bhatura","Bara"}
s1=set()
s2=set()
for i in s:
    if i.startswith("A"):
        s1.add(i)
    if i.startswith("B"):
        s2.add(i)
print(s1)
print(s2)