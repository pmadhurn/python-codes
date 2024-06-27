#program to find max between 2 nos

def Max():
    a=eval(input("enter the first value: "))
    b=eval(input("enter the second value: "))

    if a<b:
       print("{} value is biggest".format(b))
    else:
        print("{} is biggest".format(a))
#Max()

#max between 3 nos

def Max3():
    a=eval(input("enter the first value: "))
    b=eval(input("enter the second value: "))
    c=eval(input("enter the Third value: "))

    if a<b:
        if b>c:
            print("{} value is biggest".format(b))
        else :
            print("{} is biggest".format(c))
    else:
        print("{} is biggest".format(a))


#Max3()


#check for positive negitive or 0

def Chk():
    a=eval(input("enter a number : "))

    if a==0:
        print("{} is a zero".format(a))
    elif a>0:
        print("{} is positive number".format(a))
    elif a<0:
        print("{} is a negitive number".format(a))
    else:
        print("please enter a integer")

#Chk()

#wap to ckhj weather the number is divisible by 5 and 11 or not
def Chk511():
    a=eval(input("write the number that you want to check weather it is divisible by 5 and 11 or not :"))

    if a%5==0:
        if a%11==0:
            print("{} is divisible by 5 and 11".format(a))
    else:
        print("{} is not divisible by 5 and 11".format(a))
#Chk511()


#wap to check if num is evenn or odd
def Chkeo():
    a=eval(input("enter a number that you want to check : "))

    if a%2==0:
        print("{} is even".format(a))
    else:
        print("{} is odd".format(a))
#Chkeo()

#wap to check the year is leap year or not

def CkhLeapYear():
    year=int(input("Enter Year : "))
    
    if year%4==0:
        print("Leap Year")
    else:
        print("Not")

#CkhLeapYear()

#wap to check char is alphabet or not 

def Chkalp():

    cs=input("enter the character ")

    if cs<='a' and cs>='z' or cs<='A' and cs>='Z':
        print("its an alphabet")

    else:
        print("its not an alphabet") 

#Chkalp()

#wap to check weather vovel or consonent.

def CkhVC():

    cs=input("enter the character ")

    if cs=='a' or cs=='e' or cs=='o' or cs=='i' or cs=='u':
        print("print it vovel")
    else:
        print("its a consonent")

#CkhVC()

##wap to chk weather it is a alphabet,digit, or special char

def Chkads():

    cs=input("enter the thing ")

    if cs>='a' and cs<='z' or cs>='A' and cs<='Z':
        print("its an alphabet")

    elif cs<='0' and cs>='9':
        print("its a digit")

    else:
        print("its a special char")

    
#Chkads()

#wap to chk weather the char is uppercase or lower case

def ChkUL():

    cs=input("enter the Character : ")

    if cs>='a' and cs<='z':
        print("its an Lowercase alphabet")

    elif cs>='A' and cs<='Z':
        print("its an Uppercase alphabet")

    else:
        print("it not an alphabet")
#ChkUL()


##wap to input week num and print week day
def Weekday():
    
    a=int(input("enter the weekday number where the number starts from 1 = sunday: "))
    if a==1:
        print("Sunday")

    elif a==2:
        print("Monday")

    elif a==3:
        print("Tuesday")
    
    elif a==4:
        print("Wednesday")

    elif a==5:
        print("Thursday")

    elif a==6:
        print("Friday")

    elif a==7:
        print("Saturday")

    else:
        print("enter a correct number")
        

#Weekday()

##ckh days by month number
def Monthno():

    a=int(input("Enter the number of the month between 1 or 12: "))

    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        print("the month has 31 days")

    elif a==4 or a==6 or a==9 or a==11:
        print("the month has 30 days")

    elif a==2:
        print("the month has 28 days but if its a leap year then it has 29 days")

    else:
        print("wrong selection")

#Monthno()

##wap to count total no of notes in the given amount
def Notc():

    a=int(input("Enter the Amount for which you want to count the Notes: "))
    b=a%500
    c=a/500

    d=b%200
    e=b/200

    f=d%100
    g=d/100

    g=f%50
    h=f/50

    i=g%20
    j=g/20

    k=i%10
    l=i/10

    print("The Number of 500 rupee Notes will be :{:.0f}\nThe Number of 200 rupee Notes will be :{:.0f}\nThe Number of 100 rupee Notes will be :{:.0f}\nThe Number of 50 rupee Notes will be :{:.0f}\nThe Number of 20 rupee Notes will be :{:.0f}\nThe Number of 10 rupee Notes will be :{:.0f}\n".format(c,e,g,h,j,l))

#Notc()

##15wap to get angle from user and chk weather the it is a triangle or not

def Trchk():
    a=int(input("Enter the angle of the first corner : "))
    b=int(input("Enter the angle of the second corner : "))
    c=int(input("Enter the angle of the third corner : "))

    d=a+b+c

    if d==180:
        print("It is a Triangle")
    else:
        print("Its not a Trinagle")

#Trchk()

##16 wap to check if the triangle is equilateral or isosceles or scalene triangle 


def Trschk():
    a=int(input("Enter the angle of the first corner : "))
    b=int(input("Enter the angle of the second corner : "))
    c=int(input("Enter the angle of the third corner : "))

    d=a+b+c

    if d==180:

        if a==b==c==60:
            print("Its an equilateral Triangle")

        elif a!=b!=c:
            print("its an Scalene Triangle")
        else:
            print("its a isosceles triangle")
    else:
        print("its not a triangle")

#Trschk()

##wap to find roots of quadratic equation

def Root():
    import math
    a=int(input("enter the value for a for the equation ax^2+bx+c=0 : "))
    b=int(input("enter the value for b for the equation ax^2+bx+c=0 : "))
    c=int(input("enter the value for c for the equation ax^2+bx+c=0 : "))
    d=((b*b)-4*a*c)
    print (d)
    if d>0:
     e=math.sqrt(d)
    
     x=(((-b)+e)/2*a)
     y=(((-b)-e)/2*a)

     print("roots for {}x+{}y+{}=0 will be ".format(a,b,c))
     print("root 1={}".format(x))
     print("root 2={}".format(y))
     '''
     1,7,10
     '''

    elif d<0:
        print("it will have complex roots is unimaginary ") 
        '''6,11,35'''
     
    else:
        e=math.sqrt(d)
    
        x=(((-b)+e)/2*a)
    
        print("roots for {}x+{}y+{}=0 will be {} ".format(a,b,c,x))
        ''''''

#Root()

def C():
    import math
    print(math.sqrt(4))

#C()

##wap to calculate profit or loss
def Prls():
    cp=int(input("Enter the cost price of the product in rs : "))
    sp=int(input("Enter the selling price of the product in rs : "))
    if cp<sp:
        p=sp-cp
        ppr=((p/cp)*100)
        print("there is a profit of {} % or {} rs".format(ppr,p))
    elif cp>sp:
        l=cp-sp
        lpr=((l/cp)*100)
        print("there is a loss of {} % or {} rs ".format(lpr,l))
    else:
        print("There is no Profit or Loss")

#Prls()

##wap to enter the marks of 5 subjects physics ,chem,bio,comp,maths and grade them accordingly

def Mark():
    a=int(input("Enter the max marks  a student can get in each subject for all subjects : "))
    b=int(input("Enter the marks for Biology : "))
    c=int(input("Enter the marks for Physics : "))
    d=int(input("Enter the marks for Chemestry : "))
    e=int(input("Enter the marks for Maths : "))
    f=int(input("Enter the marks for Computer : "))
    
    tm=b+c+d+e+f
    per=(tm/(a*5))*100

    if per>100:
        print("invalid marks or  total marks entered")
    elif per>=90 and per<100:
        print("GARDE A")
    elif per>=80 and per<90:
        print("GARDE B")
    elif per>=70 and per<80:
        print("GARDE C")
    elif per>=60 and per<70:
        print("GARDE D")
    elif per>=40 and per<60:
        print("GARDE E")
    elif per<=40 and per>0:
        print("GARDE F")
    else:
        print("invalid marks or  total marks entered")
#Mark()

##20 wap to input basic salary of an employee adn calculate gross salary according to conditions:

def Emp():
    bs=int(input("Enter the Basic Salary of the Employee : "))

    if bs<=10000 and bs>0:
        hra=(20/100)*bs
        da=(80/100)*bs
        gs=bs+hra+da

        print("Gross salary will be : {}".format(gs))
    elif bs<=20000 and bs>=10001:
        hra=(25/100)*bs
        da=(90/100)*bs
        gs=bs+hra+da

        print("Gross salary will be : {}".format(gs))

    elif bs>=20001:
        hra=(30/100)*bs
        da=(95/100)*bs
        gs=bs+hra+da

        print("Gross salary will be : {}".format(gs))
    else:
        print("invalid input or salary")
#Emp()

##20wap to input electricity unit charges and calculate total electricity bill according to given condition

def Elebill():
    a=int(input("Enter the number of units of electricity you have consumed : "))
    if a<51 and a>0:
        t=a*0.50
    elif a>50 and a<151 :
        b=50*0.5
        c=a-50
        d=c*0.75
        t=d+b
    elif a>150 and a<251:
        b=50*0.5
        c=100*0.75
        d=a-150
        e=d*1.20
        t=c+b+e
    elif a>=250:
        b=50*0.5
        c=100*0.75
        d=100*1.20
        e=a-250
        f=e*1.50
        t=b+c+d+f
    else:
        print("please enter a valid amount of units in integer")
    
    t1=(20/100)*t
    t2=t+t1
    print("The total bill for {} units is {} rs".format(a,t2))

Elebill()






