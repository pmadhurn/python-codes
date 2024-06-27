def name1():
    name=input("please enter your name : ")
    print("welcome {}".format(name))
    opbal=eval(input("enter your opening balance : "))
    print("enter the following digits to perform corrosponding functions.")
    while True:
        op=eval(input("1\tdiposit\n2\twithraw\n3\tdisplay current balance\n4\tExit\n"))
        
        if op==1:
            a=eval(input("enter the amount you want to diposit to your account : "))
            opbal=a+opbal
            print("YOUR NEW BALANCE IS {}".format(opbal))
        elif op==2:
            b=eval(input("enter the amount you would like to withdraw from your account : "))
            if b+1000<opbal:
                opbal=opbal-b
                print("YOUR NEW BALANCE IS {}".format(opbal))
            else:
                print("sorry you hav low account balance you can not withdraw")
        elif op==3:
            print("your current availabe balance is : {}".format(opbal))
        elif op==4:
            break
        else:
            print("bad opetion")

    


acc=eval(input("please enter your account number  : " ))
if 10000000000<acc<99999999999:
    name1()
else:
    print("please enter 11 digits of account number")     
    