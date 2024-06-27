import math

def AT():


    a=eval(input("enter the length of side A : "))
    b=eval(input("enter the length of side B : "))
    c=eval(input("enter the length od side C : "))
    d=a+b+c
    s=d/2
    f=(s*(s-a)*(s-b)*(s-c))
    g=math.sqrt(f)

    print(g)

#AT()

def Distance():
    x1=eval(input("enter the location of x1 : "))
    y1=eval(input("enter the location of y1 : "))
    x2=eval(input("enter the location of x2 : "))
    y2=eval(input("enter the location of y2 : "))

    D2 = ((x2-x1)*2)+((y2-y1)*2)

    print("the distance between those points is {}".format(D2))

#Distance()

def Areaofcircle():
    
    x1=eval(input("enter the location of x1 : "))
    y1=eval(input("enter the location of y1 : "))
    x2=eval(input("enter the location of x2 : "))
    y2=eval(input("enter the location of y2 : "))

    D2 = ((x2-x1)*2)+((y2-y1)*2)

    r=D2/2
    area=(math.pi*r*r)

    print("the area of circle is : {.2f}".format(area))

#Areaofcircle()

def Conversion():
    days=int(input("ENTER THE NUMBER OF DAYS :"))
    
    
    year=int(days/365)
    
    week=days/7

    print("from the number of days {} there are {} years and {:.0f} weeks".format(days,year,week))
#Conversion()


def DEP():
    pp=eval(input("enter the prince of purchase : "))
    sp=eval(input("enter the prince of salvage : "))
    yr=int(input("enter the years of service : "))
    dep=int(((pp-sp)/yr))
    print(dep)
DEP()

def Palinatologist():
    l=eval(input("enter inductance l : "))
    r=eval(input("enter the resistance : "))
    c=eval(input("enter the capaciatance : "))

    Frequency= math.sqrt*((1/(l*c))-(r*r)/(4*c*c))

    print(Frequency)


Palinatologist() 