'''
Que1. A mechanical product based company wants to buy a machine for the company.
But the company confuse that to buy a old machine or a new machine.
So you have to help company to take a decision to by new or old machine.

A company ready to spend amount on machine per year is given below :

Machine type        Capex(capital expenditure)      Opex(operating expenditure)
Old                 10,00,000                         5,00,000
New                 20,00,000                         3,00,000
TOTAL EXPENSE= Capex+ Opex + 5%(capex)

Capex : A cost spend on machine to service it and buy it per year
Opex : A cost spend to operate a machine.

Company take decision to buy a machine based on the FINAL TOTAL PROFIT calculated for
a machine.

FINAL TOTAL PROFIT= TOTAL EXPENSE – TOTAL PROFIT BY MACHINE

If old machine have more final total profit then company buy old machine otherwise buy new
machine.

TOTAL PROFIT BY MACHINE based on below table:

machine     Income produced by machine(IC)      Profit from income produced

OLD         7,00,000<IC                               15%
            5,00,000<IC<=7,00,000                      7%
            IC<=5,00,000                               2%
NEW         15,00,000<IC                              10%
            9,00,000<IC<=15,00,000                     8%
            IC<=9,00,000                               5%

Income produced by machine entered by user

'''





def Machine():
    income=eval(input("\n\nENTER THE INCOME EARNED BY THE MACHINE : "))

    if income>0:
        print("\n\nFOR OLD MACHINE.\n")
        if 700000<income:
            profit=income*(15/100)
        elif 700000<=income<500000:
            profit=income*(7/100)
        elif income<=500000:
            profit=income*(2/100)
        else:
            print("SORRY PLEASE INSERT VALID INCOME.")
        
        capex=1000000
        opex=500000       
        expense=capex+opex+(capex*(5/100))

        totalprofitold=expense-profit

        print("FROM {} AS INCOEME YOU HAVE EARNED PROFIT OF {}".format(income,profit))
        print("YOU HAVE EXPENSE OF {} ON OLD MACHINE.".format(expense))
        

        print("\n\nFOR NEW MACHINE.\n")
        if 1500000<income:
            profitnew=income*(10/100)
        elif 900000<=income<1500000:
            profitnew=income*(8/100)
        elif income<=900000:
            profitnew=income*(5/100)
        else:
            print("SORRY PLEASE INSERT VALID INCOME.")

        capexnew=2000000
        opexnew=300000       
        expensenew=capexnew+opexnew+(capex*(3/100))

        totalprofitnew=expensenew-profitnew



        print("FROM {} AS INCOEME YOU HAVE EARNED PROFIT OF {}".format(income,profitnew))
        print("YOU HAVE EXPENSE OF {} ON NEW MACHINE.\n".format(expensenew))
        
        if totalprofitnew<totalprofitold:
            pm=totalprofitold-totalprofitnew
            print("YOU SHOULD GET THE OLD MACHINE BECAUSE IT WILL BE MORE PPROFITABLE BY {} AMOUNT.".format(pm))

        elif totalprofitnew>totalprofitold:
            pm=totalprofitnew-totalprofitold
            print("YOU SHOULD GET THE NEW MACHINE BECAUSE IT WILL BE MORE PPROFITABLE BY {} AMOUNT. ".format(pm))

        else:
            print("BECAUSE BOTH MACHINE HAVE SAME AMOUNT OF PROFITS IT WILL BE YOUR CHOICE TO GET THE MACHINE. ")
    
    else:
        print("SORRY YOU HAVE CHOSE WRONG OPTION.")

    


Machine()