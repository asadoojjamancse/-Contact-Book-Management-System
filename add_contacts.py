from save_contacts import save_contacts

def add_contact(all_contacts):
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    # Duplicate check
    for contact in all_contacts:
        if contact['Number'] == number:
            print("A contact with this phone number already exists!")
            return

    contact = {
        'Name': name,
        'Number': number,
        'Email': email,
        'Address': address
    }

    all_contacts.append(contact)
    save_contacts(all_contacts)
    print("Contact added successfully!")
