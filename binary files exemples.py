import pickle

def Q1():
    f=open("book.dat","wb")
    bookdata=createfile()
    pickle.dump(bookdata,f)
    print("Sturuccture created successfully")
    f.close()
    y=open("book.dat","rb")
    booksdata=pickle.load(y)
    displayfile(booksdata)
    y.close()
def createfile():
    
    bookdata={}
    
    while True:
        id=int(input("Enter the Id of Book : "))
        if id==0:
            break

        if id in bookdata:
            print("This ID already exists. Please use a unique ID.")
            continue

        name=input("Enter the Name of Book : ")

        author=input("Enter the Author of Book : ")

        price=int(input("Enter the Price of Book : "))

        bookdata[id]=[name,author,price]
        
    return(bookdata)



def displayfile(bookdata):
    for a,b in bookdata.items():
        print("Id of book is : ",a,"\nName of Book is : ",b[0],"\nAuthor of the ",b[0]," is : ",b[1],"\nPrice of the book is : ",b[2])


#Q1()

def studentdata():
    studentdata={}
    x=int(input("Enter the number of students whose data you want to input : "))
    y=0
    while y==x:
        y=y+1
        aid=int(input("Enter the Admission Id of the student : "))
        name=input("Enter the name of the student : ")
        per=int(input(f"Enter the percentage of the {name} : "))
        print("\n")
        studentdata[aid]=[name,per]
    print("\n\n\n")
    return{studentdata}

def Printstudents(studentdata2):
    for a,b in studentdata2.items():
        if b[1]>59:
            print("Student id : ",a,"\nName of the student : ",b[0],"\nPercentage of the student : ",b[1],"\n")
    
def Q2():
    f=open("student.dat","wb")
    studentdata=studentdata()
    pickle.dump(studentdata,f)
    print("Student details are successfully entered .")
    f.close()
    f=open("student.dat","rb")
    studentdata2=pickle.load(f)
    Printstudents(studentdata2)
    f.close()
#Q2()

def Bustdatainput():
    busdata={}
    x=int(input("Enter the number of the bus whose data you want you input : "))
    y=0
    while x==y:
        y=y+1
        busno=int(input("Enter the Bus number : "))
        sp=input("Enter the starting Point of the bus : ")
        dest=input("Enter the destination : ")
        busdata[busno]=[sp,dest]
        print("\n")
    
    print("\n\n\n")
    return(busdata)

def busprint(Busdata,destination):

    for i,j in Busdata:
        if j[1]==destination:
            print("The Bus No is {}\n".format(i))
            print("Pickup point or Starting Point is : {}".format(j[0]))
            print(f"Destination for the bus is {j[1]}")
            print("\n\n")
    print("\n\n\n\n")


def Q3():
    f=open("bus.dat","wb")
    busdata=Bustdatainput()
    pickle.dump(busdata,f)
    print("The bus dada is successfully entered in the database .")
    f.close()
    f=open("bus.dat","rb")
    a=pickle.load(f)
    f.close()
    b=input("Enter the Destination for which you want to get the data : ")
    busprint(a,b)
#Q3()