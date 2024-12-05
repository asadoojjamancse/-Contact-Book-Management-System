import csv

def save_contacts(all_contacts, filename="contacts.csv"):
    fieldnames = ['Name', 'Number', 'Email', 'Address']

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_contacts)

def load_contacts(filename="contacts.csv"):
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
