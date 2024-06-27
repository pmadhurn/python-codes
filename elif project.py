"""=>Question (30)
It’s your first day of internship at an MNC after the orientation and you really want to 
impress your seniors with your coding skills. Your manager gives you a list of tasks to 
complete before the EOD. You want to complete them as soon as possible with the 
most efficient logic so that your first impression will be great.
Understand the following cases and create programs to obtain the mentioned results.
Task 1:
Your company deals with orders from clients on a regular basis. To ensure that client 
is valid to place an order, they must be of age>18 and they must have a registered 
account with your company. Write a code to input the client’s age and username, If 
the username is “admin” then the client is registered with your company. Otherwise, 
if they are of age>18 but not with a registered account, show a message informing it 
and ask them to input a new username and password and print it.
Task 2:
Since the client is now logged in, they can place orders. Provide a list of 5 products of 
your choice with a respective price. Let the user place a single order for a single 
product only and quantity of their choice (input both product name and quantity) 
from user. Calculate the total payable amount after adding a 5% gst to the total 
amount. 
Task 3:
If the total bill amounts to one of the following categories, provide the discount as 
mentioned:
Total Amount                            Discount %
<1000                                   2   %
<2000 and greater than 1000             5   %
<3000 and greater than 2000             10  %

"""

def Main():
    age=eval(input("PLEASE ENTER YOUR AGE : "))
    if age>18:
        username=input("PLEASE ENTER YOUR USERNAME :")
        if username == "admin":
            print("YOU HAVE SUCCESSFULLY LOGGED IN TO YOUR ACCOUNT.")
            print("HERE ARE THE FOLLOWING PRODUCTS FROM OUR COMPANY:\n(NOTE THAT THE PRICES ARE WITHOUT GST)\n\n")
            print("SR. NO\t PRODUCT NAME\tPRICE")
            print("1.\tSHAMPOO\t\t800")
            print("2.\tCONDITIONER\t950")
            print("3.\tOIL\t\t100")
            print("4.\tKERITIN\t\t1200")
            print("5.\tCOMB\t\t20\n\n")
            
            #p=PRODUCT    
            p=eval(input("ENTER THE SERIAL NUMBER OF THE PRODUCT YOU WANT TO PURCHASE : "))
            
            #q=QUANTITY
            q=eval(input("ENTER THE QUANTITY OF THE PRODUCT : "))

            if p==1:
                #x=price of the product
                x=800
                y=x*q
            elif p==2:
                #x=price of the product
                x=950
                y=x*q
            elif p==3:
                #x=price of the product
                x=100
                y=x*q
            elif p==4:
                #x=price of the product
                x=1200
                y=x*q
            elif p==5:
                #x=price of the product
                x=20
                y=x*q

            else:
                print("INVALID PRODUCT SELECTED")

          
            

            if 1000>y>0:
                print("YOU ARE ELIGIBLIE FOR THE DISCOUNT OF 2% ")
                z=y*(2/100)
                
            elif 2000>y>1000:
                print("YOU ARE ELIGIBLIE FOR THE DISCOUNT OF 5% ")
                z=y*(5/100)
                
            elif y>3000:
                print("YOU ARE ELIGIBLIE FOR THE DISCOUNT OF 10% ")
                z=y*(10/100)


            else:
                print("SORRY SOMETHING WENT WWRONG.")

            
            
            #t=the payable amount after the gst and the discount 

            t= y - z

              #g=gst
            g = t * (5 / 100)
            #tp=total payable amount
            tp = g + t

            print("THE TOTAL AMOUNT FOR YOUR PURCHASED PRODUCTS WILL BE : {} RS with ".format(t))


            print("THE TOTAL PAYABLE AMOUNT IS {} Rs".format(t))            

                         
        else:
            print("YOU DO NOT HAVE A REGISTERED ACCOUNT WITH OUR CONPANY.\nTO REGISTER FOLLOW THE FOLLOWING :\n")
            username=input("ENTER YOUR NEW USERNAME : ")
            password=input("ENTER YOUR NEW PASSWORD : ")
            print("YOUR USERNAME IS : {} AND YOUR PASSWORD IS {} ".format(username,password))

        


    else:
        print("YOUR AGE MUST BE GRATER THAN 18 YEARS. ")


Main()