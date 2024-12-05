import csv

def search_contact(filename="contacts.csv"):
    search_term = input("Enter Name or Number to search: ").lower()

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

            matches = [contact for contact in contacts if search_term in contact['Name'].lower() or search_term in contact['Number']]

            if not matches:
                print("No contacts matched your search.")
                return

            print("\n--- Search Results ---")
            for contact in matches:
                print(f"Name: {contact['Name']} | Number: {contact['Number']} | "
                      f"Email: {contact['Email']} | Address: {contact['Address']}")
    except FileNotFoundError:
        print("No contacts file found! Please add some contacts first.")
