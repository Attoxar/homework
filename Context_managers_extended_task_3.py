import pytest
from Context_managers_extendet_Task_1 import FileContextManager


def process_file(file_obj):
    data = file_obj.read()

    return data.upper()


@pytest.fixture
def file_obj():
    filename = "test_file.txt"
    file_content = "This is a test file."
    with open(filename, "w") as f:
        f.write(file_content)
    with FileContextManager(filename, "r") as file:
        yield file


def test_process_file(file_obj):
    result = process_file(file_obj)
    assert result == "THIS IS A TEST FILE."