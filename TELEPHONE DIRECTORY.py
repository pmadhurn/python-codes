"""
C-TAG

Project-Based Program Task: Telephone Directory Management System
Objective:
Design and implement a Telephone Directory Management System that allows users to manage contacts efficiently. The system should support functionalities such as 
adding new contacts, updating existing contacts, deleting contacts, searching for contacts, and displaying all contacts.
Requirements:
1.	Contact Information:
o	Each contact should have the following details:
	Name (First and Last Name)
	Phone Number
	Email Address
	Address (Street, City, State, Zip Code)
2.	Functionalities:
o	Add New Contact: Allow the user to add a new contact to the directory.
o	Update Contact: Allow the user to update the details of an existing contact.
o	Delete Contact: Allow the user to delete a contact from the directory.
o	Search Contact: Allow the user to search for a contact by name or phone number.
o	Display All Contacts: Display the list of all contacts in the directory.
3.	Data Storage:
o	Use an appropriate data structure to store contact information (e.g., list, dictionary).
o	Provide an option to save the contacts to a file and load the contacts from a file to ensure data persistence between program executions.
4.	User Interface:
o	Design a simple text-based user interface (console application) that provides a menu for the user to choose different functionalities.
o	Ensure the interface is user-friendly and handles invalid inputs gracefully.
	
"""
contactlist={'Name':["Madhur","Anjali"],"Phone Number":[9016273812,8200265763],"Email Address":["pmadhurn@gmail.com","Madhur121patel.gmail.com"],"Address":["dadhavav 383462","Dantod,383642"]}
def ADDNEW():
    print("\nYOU HAVE CHOOSE ADDING NEW CONTACE SELECTION.\n")
    name=input("ENTER THE NAME OF THE CONTACT YOU WANT TO ADD : ")
    phone=input(f"ENTER THE PHONE NUMBER FOR {name} : ")    
    email=input(f"ENTER THE EMAIL ADDRESS OF FOR  {name} : ")
    address=input(f"ENTER THE ADDRESS FOR {name} IN THE FORMAT Street, City, State, Zip Code : ")
    contactlist["Name"].append(name)
    contactlist["Phone Number"].append(phone)
    contactlist["Email Address"].append(email)
    contactlist["Address"].append(address)

    
def UPDATE():
    x=input("Enter the name of the person whom you want to update : ")
    z=len(contactlist["Name"])
    x=True
    for i in range(0,z):  
            if contactlist["Name"][i]==x:
                print("found that contact\n ENTER EDITED CONTENT FOR THAT CONTACT : ")
            
                name=input(f"ENTER THE NEW NAME FOR {contactlist["Name"][i]==x}")   
                phone=input(f"ENTER THE PHONE NUMBER FOR {contactlist["Name"][i]==x} : ")    
                email=input(f"ENTER THE EMAIL ADDRESS OF FOR  {contactlist["Name"][i]==x} : ")
                address=input(f"ENTER THE ADDRESS FOR {contactlist["Name"][i]==x} IN THE FORMAT Street, City, State, Zip Code : ")
                
                contactlist["Name"][i]=name
                contactlist["Phone Number"][i]=phone
                contactlist["Email Address"][i]=email
                contactlist["Address"][i]=address
                x=False
                break
    if x:
        print("Soryy contact not found")

def DELETE():
        x=input("Enter the name of the person whom you want to Delete : ")
        z=len(contactlist["Name"])
        x=True
        for i in range(0,z):  
            if contactlist["Name"][i]==x:
                del contactlist["Name"][i]
                del contactlist["Phone Number"][i]
                del contactlist["Email Address"][i]
                del contactlist["Address"][i]
                x=False
                break    
        if x:
            print("Soryy contact not found")

def SEARCH():
    X=True
    op=int(input("Choose any one from following:\n1)\tSearch by Name.\n2)\tSearch by Phone number.\n"))
    if op==1:
            x=input("Enter the name of the person whom you want to Search : ")
            z=len(contactlist["Name"])
            for i in range(0,z):  
                if contactlist["Name"][i]==x:
                    print("Found that contact\n")
                    print("Name : ",contactlist["Name"][i])
                    print("Phone Number : ",contactlist["Phone Number"][i])
                    print("Email Address : ",contactlist["Email Address"][i])
                    print("Resedential Address",contactlist["Address"][i])
                    x=False            
                    break

            if x:
                print("Soryy contact not found")

    elif op==2:
        x=int(input("Enter the Phone number of the person whom you want to Search : "))
        z=len(contactlist["Name"])
        for i in range(0,z):
                if contactlist["Phone Number"][i]==x:
                    print("Found that contact\n")
                    print("Name : ",contactlist["Name"][i])
                    print("Phone Number : ",contactlist["Phone Number"][i])
                    print("Email Address : ",contactlist["Email Address"][i])
                    print("Resedential Address",contactlist["Address"][i])
                    x=False
                    break
        if x:
            print("Soryy contact not found")

    else:
         print("Sorry You Choose the option outside the range")
         

def DISPLAY():
    
    for i in contactlist:
        print(i," :")
        x=len(contactlist[i])
        for j in range(0,x):
            print(contactlist[i][j])
        print("\n\n",)
                        

def Main():
    while True:
        print("WELCOME TO TELEPHONE DIRECTORY MANAGEMENT SYSTEM.")
        print("\nPLEASE CHOOSE A OPETION FROM BELOW : ")
        print("\n\n\n")
        print("1. ADD NEW CONTACT.")
        print("\n2. UPDATE EXISTING CONTACT.")
        print("\n3. DELETE CONTACT.")
        print("\n4. SEARCH FOR CONTACT.")
        print("\n5. DISPLAY ALL CONTACTS.")
        print("\n6. EXIT\n\n")
        x=int(input("ENTER YOUR CHOICE : "))
        if x==1:
            ADDNEW()
        elif x==2:
            UPDATE()
        elif x==3:
            DELETE()
        elif x==4:
   
            SEARCH()
        elif x==5:
            DISPLAY()
        elif x==6:
            break
        elif x<1 and x>6:
            print("Sorry Invalid Input")
Main()