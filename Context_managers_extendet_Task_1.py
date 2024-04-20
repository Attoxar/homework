class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type is not None:
            print(f"Exception occurred: {exc_type}, {exc_value}")
        print(f"File '{self.filename}' was opened {self.counter} times.")


filename = "example.txt"

with FileContextManager(filename, "w") as file:
    file.write("Hello, world!")

with FileContextManager(filename, "r") as file:
    print(file.read())


with FileContextManager(filename, "r") as file:
    print(file.read())


try:
    with FileContextManager("nonexistent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(f"File not found: {e}")
