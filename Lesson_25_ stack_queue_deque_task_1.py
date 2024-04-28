from functools import wraps


def check_full(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_full():
            raise ValueError("storage full")
        return method(self, *args, **kwargs)
    return wrapper


def check_empty(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_empty():
            raise ValueError("storage empty")
        return method(self, *args, **kwargs)

    return wrapper


class BaseSequence:
    def __init__(self, initial_items: list, capacity=10):
        self.storage = initial_items
        self.capacity = capacity

# added the put function:

    def put(self, element):
        if self.is_full():
            raise ValueError("Storage is full")
        self.storage.append(element)

    def is_empty(self):
        return not bool(self.storage)

    def is_full(self):
        return len(self.storage) == self.capacity


class Stack(BaseSequence):
    """A LIFO (last in, first out) data structure
    put - place an item on top of the stack
    pop - remove item from the top of the stack
    is_empty - return True if it's empty
    is_full - return True if it's full
    peek - get an item from the top, but do not remove it
    """

    @check_empty
    def pop(self):
        if self.is_empty():
            raise ValueError("storage empty")
        return self.storage.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("storage empty")
        return self.storage[-1]


class Queue(BaseSequence):
    """A FIFO (first in, first out) data structure
    """
# removed the get beginning methode and replaced it with put and added the decorator
    @check_empty
    def pop(self):
        if self.is_empty():
            raise ValueError("Storage empty")
        return self.storage.pop(0)


class Dequeue(Queue, Stack):
    """
    A sequence that allows you to put and remove items from both ends
    """
# removed the get_beginning and replaced it with put_front, put_back, get_front, get back and the decorators.
    @check_full
    def put_front(self, element):
        self.storage.insert(0, element)

    @check_full
    def put_back(self, element):
        self.storage.append(element)

    @check_empty
    def get_front(self):
        if self.is_empty():
            raise ValueError("Storage empty")
        return self.storage.pop(0)

    @check_empty
    def get_back(self):
        if self.is_empty():
            raise ValueError("Storage empty")
        return self.storage.pop()

# testing the Dequeue
if __name__ == "__main__":
    dq = Dequeue([1, 2, 3, 4], 10)
    dq.put_front(0)
    dq.put_back(5)
    print(dq.get_front())  # Output: 0
    print(dq.get_back())   # Output: 5
