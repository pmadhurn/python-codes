"""file=open("madhur.txt","a")

for i in range(3):
    a=input("enter the name that you want to add in the file:")
    file.write(a+"\n")


file.close()
"""
"""
file=open("madhur.txt","r")
a=file.readlines()
for i in a:
    if str(i)==str("ruchit\n"):
        print("2")
    else:
        print(i)

"""

file=open("madhur.txt","w")
a=int(input("enter the number of employees whouse data you want to input."))
l=[]
for i in range(a):
    print(f"enter the data of employee {i+1}")
    b=input("enter the employee name : ")
    c=input("enter the emplyee salary :")
    d=input("enter the employee id : ")
    l=["\n","employee number : ",str(i+1),"\n","employee name : ",b,"\n","employee salary ",c,"\n","employee id : ",d]
    file.writelines(l)

file.close()

file=open("madhur.txt","r")
print(file.read())

