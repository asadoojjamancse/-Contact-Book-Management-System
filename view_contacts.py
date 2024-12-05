import csv

def view_contacts(filename="contacts.csv"):
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

            if not contacts:
                print("No contacts available to view.")
                return

            print("\n--- Contact List ---")
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. Name: {contact['Name']} | Number: {contact['Number']} | "
                      f"Email: {contact['Email']} | Address: {contact['Address']}")
    except FileNotFoundError:
        print("No contacts file found! Please add some contacts first.")
