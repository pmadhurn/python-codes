##input 3 numbers positive or negetive but not zero if they are unequal find the maximum otherwise display all are eqal with all positive or all negetive
def A():

        a=eval(input("Enter the first number : "))
        b=eval(input("Enter the second number : "))
        c=eval(input("Enter the third number : "))

        if a!=0 and b!=0 and c!=0:
            if a==b and a==c:
                if a>0:
                    print("All the three are greater than zero and are same.")

                else:
                    print("All the three are smaller than zero and are same.")

            else:
                if a>b and a>c:
                    print("{} or A is the greatest".format(a))
                elif b>a and c>a:
                    print("{} or B is the greatest.".format(b))
                else:
                    print("{} or C is the greatest.".format(c))
        else:
            print("There is an invalid input.")

#A()
## menu driven program

def Menu():
    a=eval(input("ENTER THE SPEED OF THE FIRST TRAIN IN MTR/S:-"))
    b=eval(input("ENTER THE SPEED OF THE SECOND TRAIN IN MTR/S:-"))
    c=eval(input("ENTER THE LENGTH OF THE FIRST TRAIN IN MTRS:-"))
    d=eval(input("ENTER THE LENGTH OF THE SECOND TRAIN IN MTRS:-"))
    e=eval(input("PRESS 1 : IF THE TRAIN IS TRAVELLING IN SAME DIRECTION \nPRESS 2 : IF THE TRAIN IS TRAVELLING IN DIFFERENT DIRECTION \nENTER YOUR CHOICE:-"))
    f=c=d
    if e==1:
            if a>b:
                g=a-b
            else:
                 g=b-a
            print("THE RELETIVE SPEED OF THE TRAINS IS {}".format(g))
            h=f/g
            print("THE TIME TAKEN BY BOTH TRAINS TO CROSS EACH OTHER WILL BE {} SEDONDS ".format(h))
                         


    elif e==2:
            g=a+b
            print("THE RELETIVE SPEED OF THE TRAINS IS {}".format(g))
            h=f/g
            print("THE TIME TAKEN BY BOTH TRAINS TO CROSS EACH OTHER WILL BE {} SECONDS ".format(h))
    else:
         print("INVALID INPUT GIVEN")


Menu()