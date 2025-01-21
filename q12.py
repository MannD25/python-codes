import math
def sas():
     radius=int(input("enter the radius "))
     x1=int(input("enter your x1"))
     x2=int(input("enter your x2"))
     if  math.sqrt(math.pow(x1,2)+math.pow(x2,2))>radius :
        print("outside the circle ")
     elif math.sqrt(math.pow(x1,2)+math.pow(x2,2))<radius :
        print("inside  the circle ")
     else:
         print("lies on the circle ")
sas()
          
          












