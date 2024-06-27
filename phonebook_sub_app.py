import os
import json

def load_phonebook(phonebook_name):
    file_path = os.path.join(os.path.dirname(__file__), f"{phonebook_name}.json")
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"No phonebook found with the name '{phonebook_name}'.")
        return []

def save_phonebook(phonebook_name, entries):
    file_path = os.path.join(os.path.dirname(__file__), f"{phonebook_name}.json")
    with open(file_path, "w") as file:
        json.dump(entries, file, indent=4)

def add_entry(entries, entry):
    entries.append(entry)

def delete_entry(entries, phone_number):
    entries = [entry for entry in entries if entry['phone_number'] != phone_number]
    return entries

def main():
    phonebook_name = input("Enter the name of the phonebook: ")
    phonebook_entries = load_phonebook(phonebook_name)

    while True:
        print("\nOptions:")
        print("1. Add new entry")
        print("2. Delete an entry")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            add_entry(phonebook_entries, {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number})
            print("Entry added successfully.")
        elif choice == '2':
            phone_number = input("Enter phone number to delete: ")
            phonebook_entries = delete_entry(phonebook_entries, phone_number)
            print("Record deleted successfully.")
        elif choice == '3':
            save_phonebook(phonebook_name, phonebook_entries)
            print("Phonebook saved successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()