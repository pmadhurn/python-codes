##INPUTS

cid=eval(input("Please Enter Your 7 digit  Customer ID  : "))
bmth=input("ENTER THE BILLING MONTH HERE IN MM-MM FORMAT : ")
rdate=input("ENTER THE READING DATE IN DD-MM-YYYY FOMATE : ")
cat=int(input("ENTER THE TYPE OF CATEGORY FOR THE BUILDING : \nTYPE 1 FOR RGP\nTYPE 2 FOR NON-RGP\nTYPE 3 FOR GLP\nTYPE 4 FOR BPL\nTYPE 5 FOR ELECTRIC VEHICLE CHARGING POINT\n\n"))
sptp=eval(input("ENTER THE SUPPLY TYPE FOR YOUR HOUSE : \nCHOOSE 1 FOR SINGLE PHASE   \nCHOOSE 2 FOR 3-PHASE \n"))
gvs=eval(input("PRESS\n1-RESEDENTIAL\n2-COMMERCIAL\n3-INDUSTRIAL\n4-RELEGIOUS\n5-HOSTEL\n5-ELECTRIC VEHICLE CHARGING POINT\n\n"))

prrd=int(input("ENTER YOUR PRESENT READING : "))
pvrd=int(input("ENTER YOUR PREVIOUS READING : "))


##CALCUALTIONS


uu=prrd-pvrd
if cat == 1:
    if uu <= 50:
        a = uu * 3.2
    elif 50 < uu <= 200:
        b = 50 * 3.20
        c = (uu - 50) * 3.95
        a = b + c
    elif uu > 200:
        b = 50 * 3.20
        c = (200 - 51) * 3.95
        d = (uu - 200) * 5
        a = b + c + d
    else:
        print("error")
        
elif cat==2:
    if uu<201:
        a=uu*4.6
    elif cat>200:
        b=200*4.6
        c=(uu-200)*7.90
        a=b+c
    else:
        print("error")
else:
    print("error wrong input")
if cat==1:
    if sptp==1:
        stptc=25
    elif sptp==2:
        stptc=65
    else:
        print("WRONG INPUT")
elif cat==2:
    if sptp==1:
        stptc=70
    elif sptp==2:
        stptc=90
    else:
        print("WRONG INPUT")
else:
    print("wrong input")

elif cat==
fppac=uu*.261
fxc=280.00
tec=a+fppac+fxc

gvdt= (20/100)*tec

ad=tec+gvdt+stptc


##OUTUPUTS
print("{: <80}".format("DEAR CUSTONER"))
print("{: ^80}".format("HERE IS YOUR TORRET POWER BILL"))

print("{: <80}".format("Customer id : "))
print(cid)
print("{: <80}".format("BILL MONTH : "+bmth))
print("{: <80}".format("READING DATE : "+rdate))

print("{: <80}".format("1 FOR RGP AND 2 FOR NON-RGP YOUR CHOICE IS : "))
print(cat)
print("{: <80}".format("1 FOR SINGLE PHASE AND 2 FOR 3-PHASE YOUR CHOICE IS : "))
print(sptp)

print("{: <80}".format("PREVIOUS READING: "))
print(pvrd)

print("{: <80}".format("CURRENT READING : "))
print(prrd)
print("{: <80}".format("CONSUMED UNITS : "))
print(uu)


print("{: ^80}".format("BILL DETAILS"))
print("ENERGY CHARGES : \t\t {:.2f} Rs".format(a))
print("FPPA CHARGES : \t\t\t {:.2f} Rs".format(fppac))
print("FIXED CHARGES: \t\t\t {:.2f} Rs".format(fxc))
print("TOTAL ENERGY CHARGES : \t\t {:.2f} Rs".format(tec))

print("GOVERNMENT DUTY : \t\t {:.2f} Rs".format(gvdt))
print("PHASE CHARGES : \t\t {:.2f} Rs".format(stptc))

print("{: ^80}".format("TOTAL AMOUNT DUE : {:.2f} Rs".format(ad)))
