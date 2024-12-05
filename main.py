from add_contacts import add_contact
from view_contacts import view_contacts
from remove_contacts import remove_contact
from search_contacts import search_contact
from save_contacts import load_contacts

# CSV file theke data load kora
all_contacts = load_contacts()

while True:
    print("\n\t\tContact Book Management System")
    print("\t\t1. Add Contact")
    print("\t\t2. View All Contacts")
    print("\t\t3. Remove Contact")
    print("\t\t4. Search Contact")
    print("\t\t0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_contact(all_contacts)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        remove_contact(all_contacts)
    elif choice == "4":
        search_contact()
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
