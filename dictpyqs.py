#write a python program to arrange values in fictionary in decending order.For exemple

def Q1():
    a={1:24,2:21,3:23}
    b=sorted(a.values())
    print(b)

#Q1()

#write a python program to join merge concate the following two dictionaries and create the new dictionary.
def Q2():
    d1={1:"Amit",2:"Suman"}
    d2={4:"Ravi",5:"Kamal"}
    x=d1|d2
    new=d1.copy()
    new.update(d2)
    print(x)

#Q2()

#write a fUnction check(key) which takes an argument if the key is present in the dictionary or not.

def check(x):
    a={1: 'Amit', 2: 'Suman', 4: 'Ravi', 5: 'Kamal'}
    print(x)
    if x in a:
        print("available")
    else:
        print("not availabe")

"""
z=4
check(z)"""

#accept the number of terms say n from the user and display the dictionary in the form of {n:n*5} for eg:
#if num entered by user is 4 then output will be {1:5,2:10,3:15,4:20}

def Q4():
    x=int(input("Enter a number .  : "))
    a={1:5}
    for i in range(2,x+1):
        z={i:i*5}
        a.update(z)

    print(a)

#Q4()

#write a program to add value of the given dictionary.
#d1={1:2,2:90,3:50}

def Q5():
    d1={1:2,2:90,3:50}
    x=0
    for i in d1:
        #print(d1[i])
        x=x+d1[i]
    
    print(x)
#Q5()


#write a program to add keys of the given dictionary.
#d1={1:2,2:90,3:50}

def Q6():
    d1={1:2,2:90,3:50}
    x=0
    for i in d1:
        #print(i)
        x=x+i

        #x=x+d1
    print(x)

#Q6()

#write a program to multiply all the values of given dictionary
#d1={1:2,2:90,3:50}
def Q7():
    d1={1:2,2:90,3:50}
    x=1
    for i in d1:
        x=x*d1[i]
        print(x)

#Q7()

##write a program to multiply all the keys of given dictionary
#d1={1:2,2:90,3:50}

def Q8():
    d1={1:2,2:90,3:50}
    x=1
    for i in d1:
        x=x*i
        print(x)
#Q8()
    
#write a progrram to take keys from user and remove that key from the dictionary if present 

def Q9():
    d1={1:2,2:90,3:50}
    x=int(input("enter the key you want to remove : "))
    if x in d1:
        d1.pop(x)
    print(d1)

#Q9() 

#write a program in python to remove the duplicate values from the dictionary.
#for eg:orignal dic={1:"Aman",2:"Suman",3:"Aman"}
def Q10():
    x={1:"Aman",2:"Suman",3:"Aman"}
    
    """for i in x:
        for j in x:
            if i==j:
                x.pop(j)
    """
    """if x==x in x:
        x.pop(x)
    """
    #working
    """y=0
    for i in x:
        for j in x:
            if i==j:
                y=j

    x.pop(y)
    print(x)
    """

    """y=[]
    for i in x:
        print("i loop: ",i)
        for j in x:
            print("j loop : ",j)
            if  x[i]==x[j]:
                if i!=j:
                    print("if loop : ", x[j])
                    y.append(j)
    print(y)
    for i in y:
        print("y loop",i)
        x.pop(i)
    print(x)
    """
    x={1:"Aman",2:"Suman",3:"Aman"}
    x1={}
    for key,value in x.items():
        if value not in x1.values():
            x1[key]=value

    print(x1)


#Q10()


"""
write a program to count number of elements in a dictionary
"""
def Q11():
    x={1:"Aman",2:"Suman",3:"Aman",4:[1,2,3,4,5,6]}
    y=len(x[4])
    z=len(y)
    print(z)
#Q10()
    

"""
accept keys from user and update its values .
"""

def Q12():

    x={1:"Aman",2:"Suman",3:"Aman",4:[1,2,3,4,5,6]}
    print(x)
    y=int(input("ENTER A VALUE FOR "))