"""""#dictionary-->{}
#d={key:value}-key is the index to  handle values

d={"season":"monsoon","fruit":["litchi","banana","pear","raspberry"],"month":["june","july","august"]}

print(len(d))
"""
"""for i in d:
    print(i," = " ,d[i])

print("---------------------------------")
""""""d1=d.copy()
print(d1)"""
"""
for k,l in d.items():
"""

""
'''
d={"C-TAG":9824502039,"Maitri":6359268920,"avin":7506992131,"Madhur":9016273812,"Kewal":9081811653}
#print(d[kewal])
x=d.get("avin")
print(x)
y=d.keys()
print(y)
d["Paras"]=9824524511
#x=d.keys()
#x=d.values()
#x=d.items()

#print(x)
if "Avin" in d:
    print("data Found")
d.update({"C-TAG":9824203104})

print(d.pop("avin"))
print(d)
print(d)
d.popitem()
print(d)

'''

#Q1 CREATE NEW DICTIONARY IN PYTHON THAT HOLDS KEY VALYE PAIRS OF FRUITS"""
def Q1():
    #d={"fruits":["apple","banana","cherry","guvava","strawberry","mango"]}
    fruits={1:"apple",2:"banana",3:"cherry",4:"guvava",5:"strawberry",6:"mango"}
    print(fruits)
#Q1()

#Q2 GET ALL THE VALUES BY KEY
def Q2():
    #d={"fruits":["apple","banana","cherry","guvava","strawberry","mango"],"veggies":["potato","brinjal",""]}
    
    fruits={1:"apple",2:"banana",3:"cherry",4:"guvava",5:"strawberry",6:"mango"}
    print(fruits)
    x=int(input("enter the key of which you wantt to find value : "))
    if x in fruits:
        print(fruits[x])
    
#Q2()


#Q3 ADD NEW KEY AND VALUES TO DICTIONARY

def Q3():
    d={1:10}
    x=input("enter key ")
    y=input("enter the value")
    d[x]=y
    for i in d:
        print(i,"=",d[i])
    print(d)

#Q3()

#Q4 REMOVE A KEY FROM DICTIONARY
def Q4():
    d={1:10,2:12,3:114,4:156}
    print(d)
    x=int(input("enter the key you want to remove from the dictionary"))
    print(d.pop(x))
    print(d)
#Q4()
#Q5 SORT PYTHON DICTIONARY BY KEY
def Q5():
    d={5:1,4:3,3:6,2:3,1:5}
    z={}
    y=sorted(d.keys())
    print(y)
    for i in y:
        x={i:d[i]}
        z.update(x)
    print(z)
#Q5()
#Q6 FIND MAXIMUN AND MININUM VALUE FROM THE DICTIONARY
def Q6():
    d={5:1,4:3,3:6,2:3,1:5}
    x=d.values()
    x=sorted(x)
    print(x)
    print("maximum : ",x[-1],"mimimum : ",x[0])
#Q6()

#Q7 MERGE TWO DICTIONARY INTO A NEW ONE
def Q7():
    d={1:10,2:12,3:114,4:156}
    e={5:6,6:7,7:8}
    f=d|e
    print(f)
#Q7()

#Q8 TEST BOTH DICTIONARY CONTENTS SPICIFIC KEY(USER DEFINED ) OR NOT
def Q8():
    d={1:10,2:12,3:114,4:156}
    e={5:6,6:7,7:8}
    f=d|e
    print(f)
    x=int(input("enter the key that you want to find"))
    y=f.keys()
    print(y)
    if x in y:
        print("available ")
    else:
        print("not available ")
#Q8()

#Q9 FIND LENGTH OF PYTHON DICTIONARY
def Q9():
    d={1: 10, 2: 12, 3: 114, 4: 156, 5: 6, 6: 7, 7: 8}
    print(len(d))

#Q9()