import unittest
import os

from Context_managers_extendet_Task_1 import (FileContextManager)


class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"
        self.file_content = "This is a test file."
        with open(self.filename, "w") as f:
            f.write(self.file_content)

    def tearDown(self):
        os.remove(self.filename)

    def test_read_file(self):
        with FileContextManager(self.filename, "r") as file:
            content = file.read()
        self.assertEqual(content, self.file_content)

    def test_write_file(self):
        new_content = "New content written."
        with FileContextManager(self.filename, "w") as file:
            file.write(new_content)
        with open(self.filename, "r") as f:
            content = f.read()
        self.assertEqual(content, new_content)

    def test_context_manager_counter(self):
        with FileContextManager(self.filename, "r") as file1:
            pass
        with FileContextManager(self.filename, "r") as file2:
            pass
        self.assertEqual(file1.counter, 1)
        self.assertEqual(file2.counter, 1)

    def test_exception_handling(self):
        with self.assertRaises(FileNotFoundError):
            with FileContextManager("nonexistent_file.txt", "r") as file:
                pass


if __name__ == "__main__":
    unittest.main()
