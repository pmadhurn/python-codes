def MENU():
    print("MENU:\nS.NO\tITEM\tPRICE\n1\tPAV BHAJI\t80.00\n2\tITALIAN PIZZA\t250.00\n3\tArabiata Pasta\t200.00\n4\tCHEESE BURGER\t40.00\n5\tJAIN BURGER\t35.00\n6\tFRENCH FRIES\t75.00\n7\tCURLEY FRIES\t85.00\n8\tTHUMS UP\t30.00\n9\tCOCA COLA\t25.00\n10\tSPRITE\t\t25.00\n")
            



def RESTAURENT():
    print("********************** Hello and welcome to Good Vibes fast food restaurant **********************")    
    amount=0
    while True:
        ch=eval(input("ENTER YOUR CHOICE:\n\t1. VIEW THE MENU\n\t2. ORDER FOOD\n\t3. EXIT\n"))
        if ch==1:
           MENU() 
        elif ch==2:
            while True:

                item=eval(input("ENTER YOUR ORDER : "))
                if item==1: 
                    print("ORDER (PAV BHAJI).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(80.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==2: 
                    print("ORDER (ITALIAN PIZZA).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(250.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==3: 
                    print("ORDER (ARABIATA PIZZA).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(200.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==4: 
                    print("ORDER (CHEESE BURGER).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(40.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==5: 
                    print("ORDER (JAIN BURGER).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(35.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==6: 
                    print("ORDER (FRENCH FRIES).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(75.00*qty)
                elif item==7: 
                    print("ORDER (CURLEY FRIES).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(85.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==8: 
                    print("ORDER (THUMBS UP).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(30.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==9: 
                    print("ORDER (COCA COLA).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(25.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.")          
                elif item==10: 
                    print("ORDER (SPRITE).")
                    qty=int(input("ENTER QUANTITY : "))
                    if qty>0:
                        amount=amount+(25.00*qty)
                    else:
                        print("PRINTED WRONG QUANTITY.") 
                more=input("WANT TO ORDER MORE GOOD FOOD.(y/n)")
                if more=='n':
                    break
            if amount<=301:
                disc=2
            elif 301<amount<600:
                disc=4
            elif 600<amount:
                disc=8

            print("calculating total order ....")
            print("amount: {}".format(amount))
            print("discount:{} %   gst : 5 %".format(disc))
         
            netamt=amount-(amount*(disc/100))+(amount*0.05)
            disca=disc/100
            print("NET AMOUNT:{}-({}*{})+({:.2f}*0.05)={}".format(amount,amount,disca,amount,netamt))
            print("THANK YOU FOR SHOPPING WITH US.\nHAVE A GREAT DAY :)")
            
            break    
        elif ch==3:
            break
            
        else:
            print("YOU CHOSE AN INCORRECT OPTION.")

RESTAURENT()

