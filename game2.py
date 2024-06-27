def Q1():
    print("What is the capital of India?")
    print("1) Ahmedabad", "\n2) London", "\n3) Mumbai", "\n4) Delhi")

def Q2():
    print("\n\n What is the largest planet in our solar system?\n")
    print("\n1) EARTH \n2) JUPITER \n3) SATURN \n4) MARS")

def Q3():
    print("\n\n What is the smallest continent by land area?\n")
    print("\n1)Asia \n2)Africa  \n3)Australia \n4)Antarctica ")


def Q4():
    print("\n\nWhat is the chemical symbol for gold? \n")
    print("\n1) Au \n2)Fe \n3)Cu \n4)Ag ")
def Q5():
    print("\n\nWhich one of these animals are gone Extint? \n")
    print("\n1) Dynasour \n2) Tiger \n3) Dogs\n4) Leopard")



def GAME():
    points=0
    a=0
    print("Welcome to the quiz Game .\n rules are simple if answer is correct you get 5 points else 3 points are deducted.\n\n")
    Q1()
    x=eval(input("PLEASE ENTER THE CHOICE OF YOUR ANSWER FORM 1 TO 4 : "))
    if x==4:
        points+=5
        print("CONGRATULATIONS, YOUR ANSWER IS CORRECT.")
        print("Your score is : ",points)

    else:
        points-=3
        print("Sorry Incorrect answer.")
        print("Your score is : ",points)


    Q2()
    x=eval(input("PLEASE ENTER THE CHOICE OF YOUR ANSWER FORM 1 TO 4 : "))
    if x==2:
        points+=5
        print("CONGRATULATIONS, YOUR ANSWER IS CORRECT.")
        print("Your score is : ",points)
    else:
        points-=3
        print("Sorry Incorrect answer.")
        
        print("Your score is : ",points)

    Q3()
    x=eval(input("PLEASE ENTER THE CHOICE OF YOUR ANSWER FORM 1 TO 4 : "))
    if x==3:
        points+=5
        
        print("CONGRATULATIONS, YOUR ANSWER IS CORRECT.")
        print("Your score is : ",points)
    else:
        points-=3
        print("Sorry Incorrect answer.")
        print("Your score is : ",points)
        

    Q4()
    x=eval(input("PLEASE ENTER THE CHOICE OF YOUR ANSWER FORM 1 TO 4 : "))
    
    if x==1:
        points+=5
        
        print("CONGRATULATIONS, YOUR ANSWER IS CORRECT.")
        print("Your score is : ",points)
    else:
        points-=3
        print("Sorry Incorrect answer.")
        print("Your score is : ",points)



    Q5()
    x=eval(input("PLEASE ENTER THE CHOICE OF YOUR ANSWER FORM 1 TO 4 : "))

    if x==1:
        points+=5
        print("CONGRATULATIONS, YOUR ANSWER IS CORRECT.")
        print("Your score is : ",points)
    else:
        points-=3
        print("Sorry Incorrect answer.")
        print("Your score is : ",points)




    print("Your Total score is : ",points)




def GAME2():
    import random
    a=random.radint(0,9)
    x=eval(input("Guess the number between 0-9 : "))
    if a==x:
        print("HURRAH! THE NUMBER YOU GUESSEED IS CORRECT.")
    else:
        print("SORRY THE NUMBER YOU GUSSED IS INCORRECT. THE CORRECT NUMBER IS :",a)

def userno():
    while True:    
        x=int(input("enter a number between 2 to 12 : "))
        if 1<x<13:
            return int(x)
        else:
            print("Invalid input. Please enter a number between 2 and 12.")

def GAME3():
    import random
    a=random.randint(2,12)
    maxtries=3
    tries=0
    print("\n\n\nWELCOME TO LUCKEY 7 GAME.\n\nHOW TO PLAY:\nYou will be prompted to enter your guess between 2 and 12. After each guess,\n you will receive feedback on whether your guess was too low, too high, or correct.\n You have three attempts to guess the lucky number.\n If you guess correctly, you win!\nIf not, the game will end after three attempts.")
    ba=eval(input("Enter the amount you want to bet : "))
    
    while tries < maxtries:
        x=userno()
        tries+=1

        if x == a:
            print(f"Congratulations! You guessed the lucky number {x}!")
            ba=ba*7
            
            print("THE BET AMOUNT THAT YOU WONIS : ",ba)
            return
        elif x < a:
            print("Too low. Try again.")
            ba=ba-(ba*0.3)
        else:
            print("Too high. Try again.")
            ba=ba-(ba*0.4)
        if tries==maxtries:
             print("Sorry, you ran out of attempts. The lucky number was {a}.")

    print("THE BET AMOUNT THAT YOU WON OR LOST IS : ",ba)
    print("Game over!") 
GAME3()