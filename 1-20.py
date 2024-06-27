##1print welcome to ctag


def Print():

    print("Welocome To C-Tag")

#Print()


##2to print an integer

def Integer():

    a=10
    print(a)

#Integer()


##3print the mailing address

def Mail():

    add="102,Broadway Street,New York,USA.10001"
    print(add)

#Mail()


##4provide border liness

def Border():


    print("\n")
    print("\n")
    print("\n")
    print("{:-^41}".format("-"))
    add="| 102,Broadway Street,New York,USA.10001"
    print(add,sep="|",end="|")
    print("{:-<42}".format("\n"))
    print("\n")
    print("\n")
    print("\n")


#Border()



##5add 2 int
def Add():

    a=10
    b=20
    print(a+b)

#Add()

##6wap to multiply 2 numbers

def Multiplication(a):
    b=10
    print(a*b)

#Multiplication(10)

##7wap to print folloing mul table

def Table(a):
    
    print(a*1)
    print(a*2)
    print(a*3)
    print(a*4)
    print(a*5)
    print(a*6)
    print(a*7)
    print(a*8)
    print(a*9)
    print(a*10)
    

#Table(10)

##8 WAP TO add and SUB 2 INT

def SUB(a,b):

    print(a+b)
    print(a-b)

#SUB(10,6)


##9 add and sum up 2 int

def Sumup(a,b):

    print(a+b)

#Sumup(6,8)



##10 add and multiply 2 integers

def AM():

    a=int(input("enter value of a"))
    b=int(input("enter the value of b"))
    c=int(input("enter the value of c"))

    print("a+b={} and b*c= {} ".format(a+b,b*c))

#AM()


##11 add and divide 2 integers

def AD():
    a=eval(input("enter value of a"))
    b=eval(input("enter value of b"))
    c=eval(input("enter value of c"))

    print("a+b={} and b/c= {} ".format(a+b,b/c))

#AD()
    
##12 to find quotent

def Qut():
    a=eval(input("enter value of a"))
    b=eval(input("enter value of b"))

    print(" quatont a/b={}".format(a/b))

#Qut()

##13 to compute remander
def Rem():
    a=eval(input("enter value of a"))
    b=eval(input("enter value of b"))

    print(" reminder a%b={}".format(a%b))

#Rem()
##14 to convert temperatue between degree celcius and faranheit

def IfDandF():

    q=int(input("1.FOOR CONVERTING CELCIUS TO FARENHEIT\n 2.FOR CONVERTING fARANHEIT TO CELCIUS\n"))
    if q==1:
        a=int(input("enter temperatue in celcius"))
        b=a*(9/5)+32

        print("temperature from celcius to Faranheit is : {}".format(b))

    elif q==2:
        a=eval(input("enter temperatue in ferienheit"))
        b=(a-32)*(5/9)

        print("temperature from faranheit to celcius is : {}".format(b))

    else:
        print("please enter values that are either 1 or 2")
#IfDandF()


##15 to convert temperatue from degree celcius to faranheit

def DtoF():
    a=int(input("enter temperatue in celcius"))
    b=a*(9/5)+32

    print("temperature from celcius to Faranheit is : {}".format(b))

#DtoF()

##16 to convert temperatue to degree celcius from faranheit

def FtoD():
    a=eval(input("enter temperatue in ferienheit"))
    b=(a-32)*(5/9)

    print("temperature from faranheit to celcius is : {}".format(b))

# FtoD()

##17 prog to convert cm to m and km

def Metrics():
    a=eval(input("enter the value in centimeters : "))
    b=a/100
    c=a/100000
    print("the {}cm in meters will be {}m and in kilometers will be {}km".format(a,b,c))

#Metrics()
    

##18 find area of circle

def CRC():
    r=eval(input("enter the radius in cm : "))
    print("the area of circle with radius {}cm will be {} cm^2 ".format(r,3.14*r*r))
CRC()

##19 find area of rectangle
def RT():
    l=eval(input("enter the length in cm : "))
    b=eval(input("enter the breath in cm : "))
    
    print("the area of Rectangle with length {}cm and Breath {} will be {} cm^2 ".format(l,b,l*b))
RT()
##20 find area off triangle
def Tr():
    h=eval(input("enter the Height in cm : "))
    b=eval(input("enter the base in cm : "))
    
    print("the area of Rectangle with Height {}cm and Base {} will be {} cm^2 ".format(h,b,h*b*.5))
Tr()