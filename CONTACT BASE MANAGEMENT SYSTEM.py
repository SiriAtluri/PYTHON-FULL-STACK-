#PROJECT
'''CONTACT BASE MANAGEMENT SYSTEM
1.ADD CONTACT
.UPDATE CONTACT
3.LIST CONTACT
4.DELTE CONTACT
5.EXIT

EG: 
NAME-> OPTION-1->
DURGASUMANTH,MOBILENO->789080....,MAILID=D@GMAIL.COM
OPTION 3-TO >DISPLAY CONTACT DETAILS
OPTION 2-> OLD MOBILE->789080,NEW MOBILE->9878989
OPTION 3->TO DISPLAY UPDATED CONTACT DETAILS
OPTION 4->NAME->POOJA->IT WILL REMOVE ENTIRE CONTACT INFORMATION
OPTION 5->EXIT'''

class Contact:
    def __init__(self):
        self.contacts = {}
# Add contact
    def add_contact(self):
        name = input("Enter name: ")
        mobile = input("Enter mobile number: ")
        email = input("Enter email: ")
        self.contacts[name] = {
            "mobile": mobile,
            "email": email
        }
        print("Contact added successfully!")
    # Update contact
    def update_contact(self):
        name = input("Enter name: ")

        if name in self.contacts:
            new_mobile = input("Enter new mobile number: ")
            self.contacts[name]["mobile"] = new_mobile

            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    # List contacts
    def list_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts available")
        else:
            for name, details in self.contacts.items():
                print("Name:", name)
                print("Mobile:", details["mobile"])
                print("Email:", details["email"])
    # Delete contact
    def delete_contact(self):
        name = input("Enter name: ")

        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
# Object creation
c = Contact()
while True:
    print("\nCONTACT MANAGEMENT SYSTEM")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        c.add_contact()
    elif choice == "2":
        c.update_contact()
    elif choice == "3":
        c.list_contacts()
    elif choice == "4":
        c.delete_contact()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
