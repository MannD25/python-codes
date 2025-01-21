list=["zero","one","two","three","fouur","five","six","seven","eight","nine","ten","eleven","twelve","thirteen"]
for i in range(0,19):
    if(i<14):
        print(list[i])
    else:
        print(list[i-10],"teen")