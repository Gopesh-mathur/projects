import os, pickle

contacts = []
CONTACTS_FILE = "contacts.dat"

def add_contact():
    print("\nAdding a new contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print(f"\nContact '{name}' added successfully!")

def view_contacts():
    print("\nAll Contacts:")
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact():
    print("\nEditing a contact:")
    view_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"Editing contact: {contact['name']}")
            new_name = input(f"Enter new name (current: {contact['name']}): ").strip()
            new_phone = input(f"Enter new phone (current: {contact['phone']}): ").strip()
            new_email = input(f"Enter new email (current: {contact['email']}): ").strip()
            contacts[index] = {"name": new_name or contact['name'], "phone": new_phone or contact['phone'], "email": new_email or contact['email']}
            save_contacts()
            print("Contact edited successfully!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact():
    print("\nDeleting a contact:")
    view_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts.pop(index)
            save_contacts()
            print(f"Contact '{contact['name']}' deleted successfully!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def save_contacts():
    try:
        with open(CONTACTS_FILE, "wb") as file:
            pickle.dump(contacts, file)
    except IOError as e:
        print(f"Error saving contacts: {e}")

def load_contacts():
    global contacts
    try:
        with open(CONTACTS_FILE, "rb") as file:
            contacts = pickle.load(file)
    except IOError:
        contacts = []

def main():
    load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
