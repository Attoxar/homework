import unittest
import os
import json
from phonebook_sub_app import load_phonebook, save_phonebook, add_entry, delete_entry


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.test_phonebook_name = "test_phonebook"
        self.test_entries = [
            {'first_name': 'John', 'last_name': 'Doe', 'phone_number': '1234567890'},
            {'first_name': 'Tim', 'last_name': 'Harald', 'phone_number': '0987654321'}
        ]
        self.test_entry_to_add = {'first_name': 'Alfred', 'last_name': 'Marly', 'phone_number': '1112223333'}
        self.test_entry_to_delete = '1234567890'

    def test_load_phonebook(self):
        file_path = os.path.join(os.path.dirname(__file__), f"{self.test_phonebook_name}.json")
        with open(file_path, "w") as file:
            json.dump(self.test_entries, file)

        loaded_entries = load_phonebook(self.test_phonebook_name)

        self.assertEqual(loaded_entries, self.test_entries)

        os.remove(file_path)

    def test_save_phonebook(self):
        save_phonebook(self.test_phonebook_name, self.test_entries)

        file_path = os.path.join(os.path.dirname(__file__), f"{self.test_phonebook_name}.json")
        with open(file_path, "r") as file:
            saved_entries = json.load(file)

        self.assertEqual(saved_entries, self.test_entries)

        os.remove(file_path)

    def test_add_entry(self):
        entries = []
        add_entry(entries, self.test_entry_to_add)
        self.assertEqual(entries, [self.test_entry_to_add])

        entries = self.test_entries.copy()
        add_entry(entries, self.test_entry_to_add)
        self.assertEqual(entries, self.test_entries + [self.test_entry_to_add])

    def test_delete_entry(self):
        entries = self.test_entries.copy()
        updated_entries = delete_entry(entries, self.test_entry_to_delete)
        self.assertEqual(updated_entries, [entry for entry in self.test_entries if entry['phone_number'] != self.test_entry_to_delete])


if __name__ == '__main__':
    unittest.main()
