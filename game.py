def game1():
    import random
    a=random.radint(0,9)
    print("SYSTEM GENERATED NUMBER = ",a)
    bamt=eval(input("enter the amount you want to bid : "))

    for i in range(0,3):
        un=eval(input("Guess the number between 0-9 : "))
        if a==un:
            print("HURRAH!!!!!!YOU ARE THE WINNER.....")
            bamt=bamt*10
            break
        else:
            print("Sorry,Better Luck Next Time")
            bamt=bamt-(bamt*0.20)
            print("AFTER DEDUCTION FINAL BID AMOUNT = ",bamt)
        print("System generated Number = ",a)
        print("Final wallet amount = ",bamt)


def Game2():
    import random
    l=["mango","banana","apple","strawberry","kiwi","litchi"]
    l1=[]
    for i in range(1,100):
        l1.append(i)
        #print(l1)
        a=random.choice(l1)
        print(a)
        random.shuffle(l1)
        print(l1)

def game3():
       import random
       l=["stone","paper","scissor"]
       cc=random.choice(l)
       uc=input("please choose from stone/paper/scessor")
       print("compuer coice =",cc)
       while True:
           if uc==cc:
               print("it's a tie try again")
               cc=random
game3()