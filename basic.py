def Q1():
    #input name,age and display on screen
    nm=input("Enter Name : ")
    age=int(input("Enter age : "))

    print(nm,"\t",age)
#Q1()

def Q2():
    import math 

    #find the area of the circle and display it
    r=eval(input("Enter the Radius : "))
    area=math.pi*r*r
    print("The Area of the circle is {:.2f}".format(area))
#Q2()

def Q3():
    import math

    #find net amount from mrp
    mrp=eval(input("Enter the MRP of the product : "))
    ds=mrp/100*10
    dmrp=mrp-ds

    gst=9/100*dmrp

    fmrp=dmrp+gst

    print("The Net Amount of the Product with 10% discount and 9% gst will be : {:.2f}".format(fmrp))

#Q3()

def Q4():

    #Enter the total number of eligible voters and from them only 80% were able to vote
    #print the number of votes got by 

    z=int(input("ENTER THE TOTAL NUMBER OF ELIGABLE VOTERS : "))

    z1=80/100*z

    x=60/100*z1
    y=40/100*z1

    print("THE X CANDIDATE GOT {} VOTES \nTHE Y CANDIDATE GOT {} VOTES.".format(x,y))

#Q4()
def Q5():
    #find net salary

    s=eval(input("Enter the Salary of the Employee : "))

    da=18/100*s
    hra=12/100*s
    cca= 10/100*s
    gs=s+da+hra+cca

    pf=8/100*gs
    ns=gs-pf

    print("The net Salary of the employee will be : {}".format(ns))

def Q5():
#ip l b h from user find area and perminteter'

l=(input("Enter Length :"))
b=(input("Enter Breath :"))
h=(input("Enter Height :"))

a=2(l*b+b*h+h*l)
p=4(l+b+h)

print("THE PERIMETER OF A CUBOID IS {} AND THE AREA IS {}".format(p,a))



#ip total amt from user and count no of notes
def Q6():
a=(input("Enter the Amount for which you want to count the Notes: "))

b=a%500
c=a/500
print(a,b,c)

Q6()