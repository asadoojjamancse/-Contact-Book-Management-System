from save_contacts import save_contacts

def remove_contact(all_contacts):
    name = input("Enter the name of the contact to remove: ")
    found = False

    for contact in all_contacts:
        if contact['Name'].lower() == name.lower():
            all_contacts.remove(contact)
            save_contacts(all_contacts)
            print(f"Contact '{name}' removed successfully!")
            found = True
            break

    if not found:
        print(f"No contact found with the name '{name}'.")
