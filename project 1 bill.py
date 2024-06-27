
import random
import os
import math


'''DATA FOR HEADER'''
brand="R&B"
add="Sarkhej - Gandhinagar Hwy,Theltej"
gst="GSTIN No. 24AACCM4949B1ZQ"
cadd="907, B Wing , 9th Floor ,Mittal Commercia,\n4th Near Mittal Commercial,Andheri-Kurlar road,Andheri(east)\nMumbai,India."
cname="Madhur N Patel"
cno=9016273812
rcno="000000N056000000438"
stid="RB012"
till="N056"
date="20-04-2024"
time="19:57"
csid="RB012"
csnm="STORE CASHIER"

'''PRINT FUNCTION FOR HEADER'''
print("{: ^80}".format(brand))
print("{: ^80}".format("LOVE IT . WEAR IT . "))
print("{: ^80}".format("Appareal Group India Pvt. Ltd"))
print("{: ^80}".format("Inovice"))
print("\n\n\n")
print("{: <80}".format(add))
print("{: <80}".format(gst))
print("{: <80}".format("Corporate Address:\n{} ".format(cadd)))
print("\n")
print("{: <80}".format("Customer Name : {}\nCustomer No. : {}".format(cname,cno)))
print("\n")
print("{: <80}".format("RECEIPT NO. : {}\nStore ID : {}\t Till : {}\n{} {} \t Cashier ID : {}\t Cashier Name : {} ".format(rcno,stid,till,date,time,csid,csnm)))

'''
data for the items
'''
i1="NAVY BLUE 7-8Y"
i1c=8909006156679
i1c2=62034200
i1q=1
i1p=599.00

i2="IVORY 13-14Y"
i2c=8909006163530
i2c2=62044220
i2q=1
i2p=899.00

i3="BLACK 13-14Y"
i3c=8909006178909
i3c2=62046200
i3q=1
i3p=699.00

i4="BLUE 13-14Y"
i4c=8909006179029
i4c2=62046200
i4q=1
i4p=699.00

i5="WHITE 13-14Y"
i5c=8909006299550
i5c2=61044200
i5q=1
i5p=499.00

i6="WHITE 7-8Y"
i6c=890900630413
i6c2=62052090
i6q=1
i6p=499.00


print("\n\nITEM_NAME\nCODE\t\tHSN\tQTY(pcs/pairs)\tMRP\tDISC%\tDISC_AMT\tGST\tNET_AMT\t\tTAX_RATE\tTAX")

print("{}\n{}\t{}\t{}\t{:.2f}\t\t\t\t\t{:.2f}\t".format(i1,i1c,i1c2,i1q,i1p,i1p))
print("{}\n{}\t{}\t{}\t{:.2f}\t\t\t\t\t{:.2f}\t".format(i2,i2c,i2c2,i2q,i2p,i2p))
print("{}\n{}\t{}\t{}\t{:.2f}\t\t\t\t\t{:.2f}\t".format(i3,i3c,i3c2,i3q,i3p,i3p))
print("{}\n{}\t{}\t{}\t{:.2f}\t\t\t\t\t{:.2f}\t".format(i4,i4c,i4c2,i4q,i4p,i4p))
print("{}\n{}\t{}\t{}\t{:.2f}\t\t\t\t\t{:.2f}\t".format(i5,i5c,i5c2,i5q,i5p,i5p))
print("{}\n{}\t{}\t{}\t{:.2f}\t\t\t\t\t{:.2f}\t".format(i6,i6c,i6c2,i6q,i6p,i6p))
print("{:_^120}".format("_"))

"""
ttl=i1p+i2p+i3p+i4p+i5p+i6p
"""
ttl=3660.95

print("Subtotal (without tax)\t\t\t\t\t\t\t\t{:.2f}".format(ttl))

txat=ttl*2.5/100

print("\n\n\nTAX\t\t\tTAXABLE AMOIUNT\t\t\tRATE\t\t\tTAX AMOUNT")
print("{: ^20}".format("CGST 2.5%\t\t{:.2f}\t\t\t\t2.5%\t\t\t{:.2f}".format(ttl,txat)))
print("sGST 2.5%\t\t{:.2f}\t\t\t\t2.5%\t\t\t{:.2f}".format(ttl,txat))

tmt=txat+ttl

print("{: ^80}".format("\nToatal Amount Paid\t\t\t\t\t\t\t\t{:.2f}".format(tmt)))

trf=437
csh=3594.00
upi=250.00
ip=i1q+i2q+i3q+i4q+i5q+i6q

print("\n\n\n\nTender\n\nCash\t\t\t{:.2f}\nTransaction ref. no.\t{}\nUPI\t\t\t{:.2f}\nTransaction ref. no.\t{}\nItem Purchased\t\t{}".format(csh,trf,upi,trf,ip))

print("\n\n\nTerms and Conditions")
print("{: ^80}".format("\nThis doncument is to be treated as tax invoice to be extent of supply of \ntaxable goods and bill of supply to the extent of supply of exempted goods .\nAll products to be exchanged must be returned in their orignal packaging \nalong with the orignal sales reciept within 14 days from the date of \npurchase (product should be in its orignal condition )"))


print("\n\n\n")
print("{: ^80}".format("{}".format(rcno)))

# # # # # print("\n\n\n")k