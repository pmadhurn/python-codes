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

'''def Q7():

    
    j=-1
    y=""
    for i in range(len(x)):
         y=y+x[j]
         j=j-1

    #y=x[::-1]
        

    print(y)'''


# Write a Python program to count the number of vowels in a string

def Q8():
    x=input("enter the string : ")
    y=0
    for i in x[::-1]:
        if i=='a'or i=='e' or i=='i' or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
                y=y+1
    
    print(y)

# Write a Python program to count the number of vowels in a string

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
    """
    for i in len(l):
        for j in range(i+1,len(l)):
            if l[i]>len[j]:
                t=l[j]
                l[j]=l[i]
                l[i]=t
    """
    sorted(l)
    print(l)

Q10()
# Write a Python program to find the sum of all elements in a given list.
def Q11():
    print("hello")
#Write a Python program to find the largest element in a given list.
# Write a Python program to find the smallest element in a given list.
# Write a Python program to find the second largest element in a given list.
# Write a Python program to find the second smallest element in a given list.
# Write a Python program to remove duplicates from a given list.
# Write a Python program to reverse a given list.
# Write a Python program to sort a given list in ascending order.
# Write a Python program to sort a given list in descending order.
# Write a Python program to find the median of a given list.
# Write a Python program to find the mode of a given list.
# Write a Python program to find the average of a given list.
# Write a Python program to find the difference between the largest and smallest elements in a given list.
# Write a Python program to find the index of a given element in a list.
# Write a Python program to find the number of occurrences of a given element in a list.
# Write a function find(name) in python to display all the names from a list of  names which are starting from alphabet 'p’.
# Write a function disp(name) in python to display all the names from a list of names whose length is of four characters.
# Write a function previous(List, name) which is accepting list of names and a name and display the index value of the first occurence of the name passed in  the list.
# Write a program in python which multiply all the numbers in the list by 3. L = ['Amit', 'Suman', 4, 8, 'Jack', 9]
# Write a program in python which add all the numbers in the list. L = ['Keyboard', 7, 'Ram', 9, 'Monitor', 11, 'Mouse' . 
#31. Write a program in python which convert all the odd numbers in the list to even by adding 1.
#32. Write a program in python which print the table of first even number. like the list is L = [23, 13, 101, 6, 81, 9, 4] so table of 6 will be printed.
#33. Write a program in python which swap the alternate members of list (assuming that even number of elements in the list). like as shown below: Original List: L = [23, 45, 67, 29, 12, 1] After Swaping : L = [45,23, 29, 69, 1, 12]
#34. Write a function mul7(list) in python which takes list as argument and multiply only those numbers which are multiples of 7.
#35. Write a program in python which concatenate all the numbers present in the list. Original List: [12, 34, 43, 2, 34] Output = 123443234
#36. Write a program in python which display only those names from the list which have 'i' as second last character. like L = ['Amit","'Suman", "Sumit", "Montu", "Anil"] Output : Amit Sumit
#37. Write a program in python which display only those names from the list Whose first character is vowel. like L = ['Amit", "Suman", "Sumit", "Montu" , "Uma", "Emil"] OUTPUT is: Amit Uma Emil
'''
# Write a program in python which removes the last element from the list and 
insert it in the beginning. like
Original List : L = [1, 3, 2, 34, 'amit', 7, 5]
News List : L = [5, 1, 3 , 2, 34, ’amit’, 7]
'''

'''# 39. Write a function countf(List, num) which takes a list of numbers and a number 
as an argument and display the frequency of that number in the list. (without 
using inbuilt function 'count)
'''

'''# 40. Write a function change(L, n) which takes a list and number as an argument and 
remove that much elements from the end of the list and add those numbers in 
the beginning of the list. 
for example
Original List : L. = [34, 23, 12, 54, 43, 89, 67]
Output List : L = [43, 89, 67, 34, 23, 12, 54 ] # if the number passed is 3
Original List: L = [34, 23, 12, 54, 43, 89, 67]
Output List: L = [54, 43, 89, 67, 34, 23, 12] # if the number passed is 4
'''

'''# 41. Write a function double(L) in python which take a list as an argument and if an 
element is numeric then multiply it by 3 and if it is a string then concatenate 
that element with itself.
for example
Original List : L = [1, 2, 'amit', 5, 'list']
Output List : L = [3, 6, 'amitamit' , 15 , 'listlist']
'''

'''# 42. Write a program that arrange all odd numbers on left side of the list and even 
numbers on the right side of the list. 
for example
Original List : L = [23, 44, 65, 78, 34, 21, 9]
Output List: L = [9, 21, 65, 23, 44, 78, 34]'''


'''# 43. Write a function disp(L) which takes a given list of five names as argument and 
display only those names which are starting from
either 'A' or 'E'. L = ('Amit", "Esha", "Sumit", "Naman", "Anuj"]'''