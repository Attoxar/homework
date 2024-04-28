class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def selection_sort(self):
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next


if __name__ == "__main__":
    linked_list = SingleLinkedList()

    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.insert(5)
    linked_list.insert(2)

    print("Original list:")
    linked_list.print_list()

    linked_list.selection_sort()

    print("Sorted list:")
    linked_list.print_list()
