def MENU():
            print("SR. NO\tITEM NAME\tPRICE")
            print("1.\tPAV BHAJI\t80.00\t")
            print("2.\tITALIAN PIZZA\t250.00\t")
            print("3.\tARABITA PASTA\t200.00\t")
            print("4.\tCHEESE BURGER\t40.00\t")
            print("5.\tJAIN BURGER\t35.00\t")
            print("6.\tFRENCH FRIES\t75.00\t")
            print("7.\tCURLEY FRIES\t85.00\t")
            print("8.\tTHUMBS UP\t30.00\t")
            print("9.\tCOCA COLA\t25.00\t")
            print("10.\tSPRITE\t\t25.00")
            

def ORDER():
    repeat = "y"
    total = 0
    while repeat == "y":
        x = int(input("ENTER YOUR ORDER :"))
        if x == 1:
            qty = int(input("ORDER(PAV BHAJI). ENTER QUANTITY: "))
            total = total + (80.00 * qty)
            repeat = input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==2:
            qty=int(input("ORDER(ITALIAN PIZZA).ENER QUANTITY: "))
            total=total+(250.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==3:
            qty=int(input("ORDER(ARABIATA PASTA).ENER QUANTITY: "))
            total=total+(200.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==4:
            qty=int(input("ORDER(CHEESE BURGER).ENER QUANTITY: "))
            total=total+(40.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==5:
            qty=int(input("ORDER(JAIN BURGER)).ENER QUANTITY: "))
            total=total+(35.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==6:
            qty=int(input("ORDER(FRENCH FRIES).ENER QUANTITY: "))
            total=total+(75.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==7:
            qty=int(input("ORDER(CURLEY FRIES).ENER QUANTITY: "))
            total=total+(85.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==8:
            qty=int(input("ORDER(THUMBS UP).ENER QUANTITY: "))
            total=total+(30.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==9:
            qty=int(input("ORDER(COCA COLA).ENER QUANTITY: "))
            total=total+(25.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ") 

        elif x==10:     
            qty=int(input("ORDER(SPRITE).ENER QUANTITY: "))
            total=total+(25.00*qty)
            repeat=input("WANT TO ORDER MORE GOOD FOOD? (y/n) : ")

        else:
            print("SORRY SOMETHING WENT WRONG .")
        
    print("CALCULATING TOTAL ORDER......\n")

    gst=5
    discount=0
    print("AMOUNT : ",total)
    if 0<total<301.00:
        discount=2
    elif 300<total<601:
        discount=4
    elif total>600:
        discount=8

    else:
        print("SORRY SOMETHING WENT WRONG .")
    print("DISCOUNT : {}\t\t\tGST : {} ".format(discount,gst))
    netamt=total-(total*(discount/100))+(total*(gst/100))
    dis=discount/100
    gst2=gst/100
    print("NET AMOUNT : {}-({}*{})+({}*{}) = {:.1f}".format(total,total,dis,total,gst2,netamt))

    print("\nTHANKYOU FOR SHOPPING WITH US.")
    print("HAVE A GREAT DAY :)")
        


        
def RESTAURENT():

    print("\n\n\n\n*********** HELLO AND WELCOME TO GOOD VIBES FAST FOOD RESTAURENNT***********")

    print("WHERE WE SERVE FOOD WITH GOOD VIBES :)")

    while True:
    
        choice=int(input("\nENTER YOUR CHOICE:\n\t1. VIEW THE MENU\n\t2. ORDER FOOD\n\t3. EXIT\n"))

        if choice==1:
            print("MENU : ")
            MENU()

            
        elif choice==2:
            ORDER()

        elif choice==3:
            print("THANK YOU FOR VISITING! HAVE A GREAT DAY!")
            break

        else:
            print("PLEASE CHOOSE CORRECT OPTION")

RESTAURENT()