def Taxdept():
    name=eval(input("Enter your name please : "))
    age=eval(input("Please Enter you age in Numbers : "))
    if age<60 and age>0:
        i=float(input("Enter your total income : "))

        if i<=250000 and i>0:
            print("you do not need to pay any taxes")

        elif i<=500000 and i>=250001:
            i1=(i-160000)
            ti=i1*(10/100)
            print("Taxable amount for {} will be {} Rs".format(name,ti))
        elif i<=1000000 and i>=500001:
            i1=(i-500000)
            ti=i1*(20/100)+34000
            print("Taxable amount for {} will be {} Rs".format(name,ti))
        elif i>=1000001:
            i1=(i-1000000)
            ti=i1*(30/100)+94000
            print("Taxable amount for {} will be {} Rs".format(name,ti))
        
    else:
        print("Sorry {} Your income does not fall into Taxable catogery.")


#Taxdept()
    
def Diposit():
    pa=float(input("Enter the amount you want to diposit : "))
    days=int(input("Enter the number of days you want to diposit money for : "))
    
    if days<=180 and days>0:
        a1=pa*(5.5/100)
        print("THE INTEREST YOU WILL GET WILL BE {} ".format(a1))

    elif days<=364 and days>181:
        a1=pa*(7.5/100)
        print("THE INTEREST YOU WILL GET WILL BE {} ".format(a1))

    elif days==365:
        a1=pa*(9/100)
        print("THE INTEREST YOU WILL GET WILL BE {} ".format(a1))

    elif days>365:
        a1=pa*(8.5/100)
        print("THE INTEREST YOU WILL GET WILL BE {} ".format(a1))

    else:
        print("Please enter a positive amount")

    ma=a1+pa

    print("The maturity amount will be : {} rs ".format(ma))
#Diposit()

def Lic():
    name=input("Enter the name of  Policy holder : ")
    sa=int(input("Please enter the sum ensured by LIC: "))
    f=int(input("enter the Amount of first annual premium"))
    if sa<=100000:
        a=sa*(5/100)
        b=sa*(2/100)
        p=sa-a
    elif sa>=100001 and sa<=200000:
        a=sa*(8/100)
        b=sa*(3/100)
        p=sa-a
    elif sa>=200001 and sa<=500000:
        a=sa*(10/100)
        b=sa*(5/100)
        p=sa-a        
    elif sa>=500001:
        a=sa*(15/100)
        b=sa*(7.5/100)
        p=sa-a
    else:
        print("invalid amount written")

    print("NAME OF POLICY HOLDER : {}".format(name))
    print("Sum assured : {}".format(sa))
    print("Premium : {}".format(p))
    print("Discount on FIrst Premium : {}".format(a))
    print("Commission of the agent : {} ".format(b))

#Lic()

def Comp():
    name=input("Please enter your name : ")
    a=eval(input("Enter your Basic salary : "))
    if a<=10000:
        da=a*(10/100)
        sa=a*(5/100)

    elif a<=20000 and a>10000:
        da=a*(12/100)
        sa=a*(8/100)

    elif a<=30000 and a>20000:
        da=a*(15/100)
        sa=a*(10/100)

    elif a>30001:
        da=a*(20/100)
        sa=a*(12/100)

    else:
        print("invalid amount written")

    gs=a+sa+da
    print("Name\tBasic\tDa\tSpl. Allowance\tGross Salary")
    print("{}\t{}\t{}\t{}\t\t{}".format(name,a,da,sa,gs))

Comp()
