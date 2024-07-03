"""
C-TAG

Project-Based Program Task: Telephone Directory Management System
Objective:
Design and implement a Telephone Directory Management System that allows users to manage contacts efficiently. The system should support functionalities such as adding new contacts, updating existing contacts, deleting contacts, searching for contacts, and displaying all contacts.
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
import os

class Contact:
    def __init__(self, first_name, last_name, phone_number, email, street, city, state, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class TelephoneDirectory:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.txt"
        self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def update_contact(self, index, contact):
        self.contacts[index] = contact
        self.save_contacts()

    def delete_contact(self, index):
        del self.contacts[index]
        self.save_contacts()

    def search_contact(self, query):
        return [contact for contact in self.contacts 
                if query.lower() in contact.first_name.lower() 
                or query.lower() in contact.last_name.lower() 
                or query in contact.phone_number]

    def display_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. {contact.first_name} {contact.last_name} - {contact.phone_number}")

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            for contact in self.contacts:
                f.write(str(contact.to_dict()) + '\n')

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    contact_dict = eval(line.strip())
                    self.contacts.append(Contact.from_dict(contact_dict))

def get_contact_details():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    street = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    return Contact(first_name, last_name, phone_number, email, street, city, state, zip_code)

def main():
    directory = TelephoneDirectory()

    while True:
        print("\nTelephone Directory Management System")
        print("1. Add New Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = get_contact_details()
            directory.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            directory.display_contacts()
            index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= index < len(directory.contacts):
                contact = get_contact_details()
                directory.update_contact(index, contact)
                print("Contact updated successfully!")
            else:
                print("Invalid contact number!")

        elif choice == '3':
            directory.display_contacts()
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(directory.contacts):
                directory.delete_contact(index)
                print("Contact deleted successfully!")
            else:
                print("Invalid contact number!")

        elif choice == '4':
            query = input("Enter name or phone number to search: ")
            results = directory.search_contact(query)
            if results:
                print("Search results:")
                for contact in results:
                    print(f"{contact.first_name} {contact.last_name} - {contact.phone_number}")
            else:
                print("No contacts found!")

        elif choice == '5':
            directory.display_contacts()

        elif choice == '6':
            print("Thank you for using the Telephone Directory Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

main()