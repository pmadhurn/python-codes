#Write a Python program to print "Hello, World!" to the console.


def Q1():
    print("Hello, World!")

#Write a Python program to add two numbers and print the result to the console


def Q2():
    a=10
    b=20
    print(a+b)

#Write a Python program to find the maximum of two numbers.

def Q3():
    a=10
    b=20
    if a>b:
        print(a," is the greatest number.")
    else:
       print(b," is the gratest number.")

#Write a Python program to find the sum of all elements in a list.

def Q4():
    l=eval(input("enter the numerical elements for the list:"))
    x=0
    for i in l:
       x=x+i
       print("the sum of the list is :",x)

# Write a Python program to print the first n Fibonacci numbers.

def Q5():
    a=0
    b=1
    c=0
    
    x=int(input("Enter the number n: "))
    print(a,b,sep="  ",end="  ")
    while c<=x:
            c=a+b
            a=b
            b=c
            print (c,end="  ")

#Write a Python program to check if a number is prime or not
    
def Q6():
    x=eval(input("enter the number you wnat to check if it is prime or not : "))
    y=0
    for i in range(2, x):
        if x%i==0:
            y=1

    
    if y==1:
        print(x," is not prime number")
    elif y==0:
        print(x," is a prime number.")
    else:
        print("error")

# Write a Python program to reverse a string.

def Q7():
    x=input("enter a string")
    #length=len(x)
    j=-1
    y=""
    """for i in range(length):
         y=y+x[j]
         j=j-1
            """
    y=x[::-1]
        

    print(y)





# Write a Python program to count the number of vowels in a string

def Q8():
    x=input("enter the string : ")
    y=0
    for i in x[::-1]:
        if i=='a'or i=='e' or i=='i' or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
                y=y+1
    
    print(y)

# Write a Python program to check if a string is a palindrome or not.

def Q9():
    x=input("enter the string : ")

    if x==x[::-1]:
        print("its palindrome.")
    else:
        print("not palindorme.")



# Write a Python program to sort a list of numbers in ascending order.

def Q10():
    l=eval(input("enter the list of number : "))
    t=0
    
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                t=l[j]
                l[j]=l[i]
                l[i]=t
    
    sorted(l)
    print(l)


# Write a Python program to find the sum of all elements in a given list.
def Q11():
    x=eval(input("enter the list of the numbers : "))
    s=sum(x)
    print("The sum is ",s)


#Write a Python program to find the largest element in a given list.


def Q12():
    x=eval(input("enter the list of the numbers : "))
    y=max(x)
    print("THE LARGEST NUMBER IN THE LIST IS : ",y)

# Write a Python program to find the smallest element in a given list.

def Q13():
    x=eval(input("ENTER THE LIST : "))
    y=min(x)
    print("THE SMALLEST NUMBER IS :",y)

# Write a Python program to find the second largest element in a given list.

def Q14():
    x=eval(input("ENNTER THE LIST : "))
    x=sorted(x)
    print("the second largest number is ",x[-2])

# Write a Python program to find the second smallest element in a given list.

def Q15():    
    x=eval(input("ENNTER THE LIST : "))
    x=sorted(x)
    print("the second smallest number in the list is : ",x[1])

# Write a Python program to remove duplicates from a given list.

def Q16():
    x=eval(input("ENNTER THE LIST : "))
    x=sorted(x)
    i=0
    while i<len(x)-1:
        if x[i]==x[i+1]:
            del x[i]
        else:
            i+=1
    print(x)


# Write a Python program to reverse a given list.
def Q18():

    x=eval(input("ENNTER THE LIST : "))
    y=x[::-1]
    print(y)

# Write a Python program to sort a given list in ascending order.
def Q19():
    x=eval(input("enter the list :"))
    y=sorted(x)
    print(y)

# Write a Python program to sort a given list in descending order.
def Q20():
    x=eval(input("enter the list :"))
    y=sorted(x)
    z=y[::-1]
    print(z)

# Write a Python program to find the median of a given list.

def Q21():
    x=eval(input("enter the list : "))
    y=len(x)
    if x%2==0:
        print("median is ",x[x/2])
    elif x%2==1:
        print("median is ",x[(x/2)+0.5]," or ",x[(x/2)-0.5])
    else:
        print ("error") 


# Write a Python program to find the mode of a given list.

 

"""  
    x = eval(input("Enter the list: "))
    x = sorted(x)
    unique_items = set(x)
    mode = None
    max_count = 0
    
    for item in unique_items:
        count = x.count(item)
        if count > max_count:
            max_count = count
            mode = item
    
    if max_count == 1:
        print("There is no mode in the given list.")
    else:
        print(f"The mode of the list is: {mode}")
"""
def Q22():   
    import statistics as s 
    print(dir(s))
    l=[1,2,3,2,1,4,5,6,7,4,3,2,1,2,2,3,4,1,5,6,7,8,9]
    a=s.mode(l)
    print("Mode = ",a)


#Q22()

# Write a Python program to find the average of a given list.
def Q23():   
    x=eval(input("enter the list : "))
    y=sum(x)
    t=len(x)
    z=y/t
    print(z)

# Write a Python program to find the difference between the largest and smallest elements in a given list.

def Q24():   
    x=eval(input("enter the list : "))
    y=sorted(x)
    z=x[-1]-x[0]
    print(z)

# Write a Python program to find the index of a given element in a list.

def Q24():   
    x=eval(input("enter the list : "))
    z=eval(input("enter the number : "))
    i=0
    for i in len(x):
        if x[i]==z:
            print(i)
        else:
            print("loading")

# Write a Python program to find the number of occurrences of a given element in a list.

def Q25():
    x=eval(input("enter the list : "))
    y=eval(input("enter the enement you want to count in the lsit. "))

    z=0

    z=x.count(y)

    print("OCCURANCCE OF ",y,"int the list is ",z)

def Count2():
    x=eval(input("enter the list : "))
    y=eval(input("enter the enement you want to count in the lsit. "))
    z=0

    for i in x:
        if y==i:
            z=z+1
    
    print("OCCURANCCE OF ",y,"int the list is ",z)


#Write a function find(name) in python to display all the names from a list of  names which are starting from alphabet 'p’.

"""
def FINDNAME():
    names=[input("ENTER THE NAMES SEPERATED BY COMMA and in quotes.")]

    for i in range(names):
        for j in names[i]:
            """

def Find(name):
    for i in name:
        if i[0]=='p':
            print(i)
        else:
            print("NAME NOT AVAILABLE IN THE LIST.")


#names=["anjali","paul","madhur","raghav","priyanka","pista","hola"]
#Find(names)


#Write a function disp(name) in python to display all the names from a list of  names whose length is of four characters.


def Disp():
    names=["anjali","paul","madhur","raghav","priyanka","pista","hola"]
    for i in names:
        if len(i)==4:
            print(i)

#Disp()


#Write a function previous(List, name) which is accepting list of names and a name and display the index value of the first occurence of the name passed in 
#the list.

def PREVIOUS(List, name,length):
    for i in range(length):
        if List[i]==name:
            print("the index value of first occurance of ",name," is ",i)
            break




"""
x=["anjali","paul","madhur","raghav","priyanka","pista","hola"]
y=input("ENTER THE NAME YOU WANT TO SEARCH IN THE LIST.")
z=len(x)
PREVIOUS(x,y,z)
"""

"""
Write a program in python which multiply all the numbers in the list by 3.
L = ['Amit', 'Suman', 4, 8, 'Jack', 9]
"""

def Q29():
    L = ['Amit', 'Suman', 4, 8, 'Jack', 9]
    for i in L:
        if type(i)==int:
            print(i*3)

#Q29()


"""
Write a program in python which add all the numbers in the list.
L = ['Keyboard', 7, 'Ram', 9, 'Monitor', 11, 'Mouse']

"""

def Q30():
    L = ['Keyboard', 7, 'Ram', 9, 'Monitor', 11, 'Mouse']
    z=0

    for i in L:
        if type(i)==int:
            z=z+i
    print("sum is : ",z)

#Q30()

"""
Write a program in python which convert all the odd numbers in the list to even 
by adding 1."""

def Q31():
    l=eval(input("enter the list of numbers."))
    for i in range(len(l)):
        if l[i]%2==1:
            l[i]=l[i]+1
    
    print(l)

#Q31()

"""
Write a program in python which print the table of first even
number. like the list is L = [23, 13, 101, 6, 81, 9, 4] so table of 6 will
be printed
"""

def Q32():
    x=eval(input("enter the list."))
    for i in range(len(x)):
        if x[i]%2==0:
            for j in range(10):
                print(j,"*",x[i],"=",j*x[i])
            break

#Q32()


"""
Write a program in python which swap the alternate members of list (assuming 
that even number of elements in the list). 
like as shown below:
Original List: L = [23, 45, 67, 29, 12, 1]
After Swaping : L = [45,23, 29, 69, 1, 12]
"""

def Q33():
    x=[23, 45, 67, 29, 12, 1]
    y=len(x)-1
    z=[]
    
    for i in range(0,y,2):
        z.append(x[i+1])
        z.append(x[i])
        
    print(x)
    print(z)

#Q33()

"""
Write a function mul7(list) in python which takes list as argument and multiply 
only those numbers which are multiples of 7"""


def mul7(list):
    x=list
    y=1
    z=len(x)
    for i in range(z):
        if x[i]%7==0:
            y=y*(x[i])

    print(y)
    


"""
l=eval(input("enter the list."))
#[1,7,2,14,3,21,4,28]

mul7(l)"""

"""
Write a program in python which concatenate all the numbers present in the 
list.
Original List: [12, 34, 43, 2, 34]
Output = 123443234"""

def Q35():
    a=''
    l=[12, 34, 43, 2, 34]
    for i in l:
        a=a+str(i)
    print(a)   

 

"""
Write a program in python which display only those names
from the list which have 'i' as second last character. like L = ['Amit",
"'Suman", "Sumit", "Montu", "Anil"]
Output :
Amit
Sumit
"""

def Q36():
    l=["Amit","Suman", "Sumit", "Montu", "Anil"]
    for i in l:
        if i[-2]=="i":
            print(i)

"""
Write a program in python which display only those name
from the list Whose first character is vowel. like L = ['Amit",
"Suman", "Sumit", "Montu" , "Uma", "Emil"]
OUTPUT is:
Amit
Uma
Emil
"""

def Q37():
    l=["Amit","Suman", "Sumit", "Montu" , "Uma", "Emil"]
    for i in l:
        if i[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            print(i)


"""
Write a program in python which removes the last element from the list and 
insert it in the beginning. like
Original List : L = [1, 3, 2, 34, 'amit', 7, 5]
News List : L = [5, 1, 3 , 2, 34, ’amit’, 7]
"""
def Q38():
    l = [1, 3, 2, 34, 'amit', 7, 5]
    x=len(l)-1
    y=l[x]
    l.remove(y)
    l.insert(0,y)
    print(l)
    



"""
Write a function countf(List, num) which takes a list of numbers and a number 
as an argument and display the frequency of that number in the list. (without 
using inbuilt function 'count)
"""

def COUNTF(l,n):
    x=0
    for i in l:
        if i==n:
            x=x+1
    
    print(x)

    
list = [1,2,3,4,5,6,7,8,9,2,3,4,5,4,3,2,6,8,5]
num=4
#COUNTF(list,num)

"""
Write a function change(L, n) which takes a list and number as an argument and 
remove that much elements from the end of the list and add those numbers in 
the beginning of the list. 
for example
Original List : L. = [34, 23, 12, 54, 43, 89, 67]
Output List : L = [43, 89, 67, 34, 23, 12, 54 ] # if the number passed is 3
Original List: L = [34, 23, 12, 54, 43, 89, 67]
Output List: L = [54, 43, 89, 67, 34, 23, 12] # if the number passed is 4
"""
def CHANGES(l,n):
    
    for i in range(n): 
        x=len(l)-1
        y=l[x]
        l.remove(y)
        l.insert(0,y)
    print(l)
        
"""list=[34, 23, 12, 54, 43, 89, 67]
number=3
CHANGES(list,number)
"""
"""
Write a function double(L) in python which take a list as an argument and if an 
element is numeric then multiply it by 3 and if it is a string then concatenate 
that element with itself.
for example
Original List : L = [1, 2, 'amit', 5, 'list']
Output List : L = [3, 6, 'amitamit' , 15 , 'listlist']
"""
def DOUBLE(l):
    print(l)
    x=len(l)
    for i in range(x):
        if type(l[i])==int:
            l[i]=l[i]*3
        if type(l[i])==str:
            l[i]=l[i]+l[i]
        
    print(l)
"""
L = [1, 2, 'amit', 5, 'list']
DOUBLE(L)
"""
"""
Write a program that arrange all odd numbers on left side of the list and even 
numbers on the right side of the list. 
for example
Original List : L = [23, 44, 65, 78, 34, 21, 9]
Output List: L = [9, 21, 65, 23, 44, 78, 34]
"""
def Q42():
    l = [23, 44, 65, 78, 34, 21, 9]
    y=len(l)
    for j in range(y):
            if l[j]%2==1:
                x=len(l)-1
                y=l[j]
                l.remove(y)
                l.insert(0,y)
                
    print(l)

#Q42()

"""
Write a function disp(L) which takes a given list of five names as argument and 
display only those names which are starting from
either 'A' or 'E'. L = ('Amit", "Esha", "Sumit", "Naman", "Anuj"]
"""
def disp(l):
    for i in l :
        if i[0] in ["E","A"]:
            print(i)
    
"""L = ["Amit", "Esha", "Sumit", "Naman", "Anuj"]
disp(L)
"""