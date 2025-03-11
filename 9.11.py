l1=[1,2,3,4,5,3,2,3]
l2=[3,2,1,4,5]
def create_list(l1, l2):
    s1=set(l1)
    s2=set(l2)
    s=s1.intersection(s2)
    return list(s)
print(create_list(l1, l2))
