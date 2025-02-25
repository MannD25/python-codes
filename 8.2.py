import random

s=set()
count=0
for i in range(0,9):
    s.add(random.randint(15,45))
for i in s.copy():
    if i>35:
        s.discard(i)
for i in s:
    if i<30:
        count+=1
print(s)
print(count)