#Write a program in Python to Find all prime numbers in a given list

def is_prime(num):
    import math
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def Q1():
    
    n=int(input("ENTER THE LENGTH OF THE LIST : "))
    l=[]
    for i in range(0,n):
        x=eval(input(f"Enter the Element {i} for the list : "))
        l.append(x)  
    

    for i in l:
        z=is_prime(i)
        if z:
            print(f"{i} is a Prime Number")   
Q1()



#Write a python program to print the length of each element in the given list.
def Q2():
    n=int(input("ENTER THE LENGTH OF THE LIST : "))
    l=[]
    for i in range(0,n):
        x=input(f"Enter the Element {i} for the list : ")
        l.append(x)
    for i in l:
        print(f"Length of {i} is {len(i)}")

#Q2()   
#Write a python program to Find longest string in given list.
def Q3():
    n=int(input("ENTER THE LENGTH OF THE LIST : "))
    l=[]
    for i in range(0,n):
        x=input(f"Enter the Element {i} for the list : ")
        l.append(x)
    q=0

    for i in range(len(l)):
        y=len(l[i])
        if y>q:
            q=i

    print(f"The Longest String in the list is {l[q]}")    
#Q3()



#Write a Python program to split a list of string in to list of characters.
def Q4():
    x=input("Enter a string which needs to be split : ")
    y=[]
    for i in x:
        y.append(i)
    print(y)
#Q4()


#Write a Python program to find string palindrome in a list and then print all string palindrome in ascending order.
def Q5():
    x=input("Enter a string which needs to be checked if its palindrome or not : ")
    if x[::1]==x[::-1]:
        print(f"String {x} is Palindrome")
    else:
        print(f"String {x} is not Palindrome")   
#Q5()
