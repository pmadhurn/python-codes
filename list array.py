def Q1():
    l=[11,33.5,40,[1,2,3],9,4.5,3,6,[6,'abc']]
    print(l[3][2])
    l1=['x','y','z']
    l.extend(l1)
    n=eval(input("Enter N :"))

    for i in range(n):
        val=eval(input("ENTER :"))
        l.append(val)

    print(l)

def Q2():
    l=[1,5,3,4,2,6,7,8]
    for i in (l):
        print(i)

def Q3():
    q=[]
    x=eval(input("enter the size of the list : "))
    for i in range(x):
        z=eval(input("enter the number : "))
        q.append(z)

    for i in x:
        if i%10==2:
            print(i)

def Q4():
    l=input("ENTER YOUR FIRST AND LAST NAME")
    print(l)
   
    print(l[1:5],"  ",l[7:9])

    y=l[::-1]
    print(y)

#count nuber of times a character can occur entered by the user:

def Q5():
    x=input("enter the string : ")
    y=input("enter the char you want to cheak the occurance of : ")
    z=0
    for i in x:
        if i==y:
            z+=1
    
    print("the number of occurance of ",y,"will be ",z)


#cheak if the string is palindrome or not.

def Q6():
    l=input
    if l==l[::-1]:
        print("string is palindrome .")
    else:
        print("String is not palindrome.")



#input string having some digits find sum of digits in the string .
"""
def Q7():
    a=input("enter the string : ")
    x=list(a)
    z=0
    for i in x:
        if type(i)==int:
            z=int(i)+z
        
    print(z)

Q7()
"""

def Q7():
    a=input("enter the string : ")
    x=list(a)
    print(x)
    z=0
    for i in x:
        if 47<ord(i)<58:
            z=eval(i)+z
    print(z)

Q7()