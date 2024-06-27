
def Laptop():
    name=input("ENTER YOUR NAME : ")
    price=eval(input("ENTER THE PRICE OF THE LAPTOP : "))
    print("DEAR {}\n".format(name))

    if 0<price<50000:
        dis=price*(7.5/100)
    elif 50000<price<100000:
        dis=price*(10/100)
    elif 100000<price:
        dis=price*(15/100)
    price=price-dis
    print("YOU ARE ELIGIBLE TO GET DISCOUNT OF : {:.2f} RS".format(dis))
    
    gst=price*(18/100)

    netpa=price+gst

    print("THE NET PRICE OF THE LAPTOP WOULD BE {:.2f} RS".format(netpa))

Laptop()

def SUCCSIVE():
    price=eval(input("ENTER THE PRICE OF THE PRODUCT : "))
    d1=eval(input("ENTER THE FIRST DISCOUNT : "))
    d2=eval(input("ENTER THE SECOND DISCOUNT : "))

    a=price*(d1/100)
    price=price-a

    print("PRICE AFTER THE FIRST DISCOUNT {:.2f} RS ".format(price))
    
    a=price*(d2/100)
    price=price-a

    print("PRICE AFTER BOTH DISCOUNT {:.2f} RS".format(price))


SUCCSIVE()

def MENUAREA():
    mn=input("TO CALCULATE THE AREA OF CIRCLE ENTER  c \nTO CALCUALE THE AREA OF SQUARE ENTER  r \nTO CALCUALATE THE AREA OF RECTANGLE ENTER  r ")
    if mn == 'c':
        a=eval(input("ENTER RADIUS"))
        area=a*a*3.14
        print("area of circle is {:.2f}".format(area))
    elif mn=='s':
        a=eval(input("ENTER THE LENGTH OF THE SIDE"))
        area=a*a
        print("THE AREA OF SQUARE IS {:.2f}}".format(area))
    elif mn=='r':
        a=eval(input("ENTER THE LENGTH OF RECTANGLE : "))
        b=eval(input("ENTER THE BREATH OF RETANGLE"))
        area=a*b
        print("THE AREA OF RECTANGLE IS {:.2f}".format(area))
    else:
        print("wrong option")
MENUAREA()

def CUBE():
    a=eval(input("TYPE \n1 FOR CUBE \n2 FOR SPHERE \n3 FOR CUBOID\n"))
    if a==1:
        s=eval(input("ENTER THE LENGTH OF THE SIDE"))
        area=s*s*s
        print("THE AREA OF CUBE IS {} ".format(area))
    elif a==2:
        r=eval(input("ENTER THE RADIUS : "))
        area=(4/3)*r*r*r*3.14
        print("THE AREA OF SPHERE IS {}".format(area))
    elif a=='3':
        l=eval(input("ENTER THE LENGTH OF CUBOID : "))
        b=eval(input("ENTER THE BREATH OF CUBOID : "))
        h=eval(input("ENTER THE HEIGHT OF CUBOID : "))

        area=b*l*h
        print("THE AREA OF CUBOID IS {:.2f}".format(area))
    else:
        print("wrong option")

CUBE()


def RV():
    a=eval("enter the velocity of train 1 in m/s : ")
    b=eval("enter the velocity of train 2 in m/s : ")
    x=eval(input("IF THE TRAINS ARE TRAVELLING IN SAME DIRECTION TYPE 1 ELSE TYPE 2 : "))
    len1=eval(input("enter the length  of train 1 in mtr : "))
    len2=eval(input("enter the length  of train 2 in mtr : "))
    
    length=len1+len2

    if x==1:
        if a>b:
            c=a-b
        elif a<b:
            c=b-a
        else:
            print ("no trains can pass each other ")

        print("reletive velociity between the trains is {} m/s".format(c))
        time=c/length

        print("the time taken to cross both train will be {}".format(time))

    elif x==2:
        
        c=a+b
        print("reletive velociity between the trains is {} m/s".format(c))
        
        time=c/length
        print("the time taken to cross both train will be {}".format(time))

    else:
        print("wrong option")

RV()

def CAR():
    price=eval(input("enter the ex showroom price of the car : "))
    age=int(input("enter the age of the car : "))
    
    if age==1:
        dep=price*(10/100)
        atp=price-dep
        print("THE ORIGNAL PRICE IS {} RS \nTHE AGE IS {} \nTHE DEPERIATED VALUE OF THE CAR IS {}\nTHE PRICE AFTER THE DEPERIATION IS {} RS".format(price,age,dep,atp))
    elif age==2:
        dep=price*(20/100)
        atp=price-dep
        print("THE ORIGNAL PRICE IS {} RS \nTHE AGE IS {} \nTHE DEPERIATED VALUE OF THE CAR IS {}\nTHE PRICE AFTER THE DEPERIATION IS {} RS".format(price,age,dep,atp))
    elif age==3:
        dep=price*(30/100)
        atp=price-dep
        print("THE ORIGNAL PRICE IS {} RS \nTHE AGE IS {} \nTHE DEPERIATED VALUE OF THE CAR IS {}\nTHE PRICE AFTER THE DEPERIATION IS {} RS".format(price,age,dep,atp))
    elif age==4:
        dep=price*(40/100)
        atp=price-dep
        print("THE ORIGNAL PRICE IS {} RS \nTHE AGE IS {} \nTHE DEPERIATED VALUE OF THE CAR IS {}\nTHE PRICE AFTER THE DEPERIATION IS {} RS".format(price,age,dep,atp))
    elif age>4:
        dep=price*(50/100)
        atp=price-dep
        print("THE ORIGNAL PRICE IS {} RS \nTHE AGE IS {} \nTHE DEPERIATED VALUE OF THE CAR IS {}\nTHE PRICE AFTER THE DEPERIATION IS {} RS".format(price,age,dep,atp))
    else:
        print("wrong age")

CAR()


def SA():
    ac=eval(input("enter the opening balance : "))
    ch=0
    while True:
        ch=eval(input("1.MONEY DIPOSIT\n2.MONEY WITHDRAWN\n3.CHECK BALANCE\n4.QUIT \n\nENTER THE APPROPRITE OPTION : "))
        if ch==1:
            a=eval(input("enter the amount you want to diposit : "))
            ac=ac+a
            print("diposit successful")
        elif ch==2:
            a=eval(input("enter the amount you want to withdraw : "))
            if a>ac or a<0:
                print("invalid amount entered or insufficient balance.")
            else:
                ac=ac-a
                print("withdrawl successful.")
        elif ch==3:
            print("your account balance is {} RS".format(ac))
        elif ch==4:
            break
        else:
            print("bad value.")
SA()

