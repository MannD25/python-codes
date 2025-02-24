t=(1,2,4,56,7,'hell',)
List=list(t)
for i in range(0,len(List)):
    if List[i]=='' or List[i]==NotImplemented:
        List.pop(i)
print(List)
