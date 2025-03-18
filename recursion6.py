
def santize(user,index=0):
    if user[index]==len(user):
        return user
    if user[index]<0:
        user[index]=0
    return santize(user ,index+1)
user=[-1,2,-3,-4,5]
print(santize(user))