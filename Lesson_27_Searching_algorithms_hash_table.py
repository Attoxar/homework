import string

ASCII_MAPPING = {}
INDEX = 0
for letter in string.ascii_letters + "0123456789 ,.!?()[]":
    ASCII_MAPPING[letter] = INDEX
    INDEX += 1


def hash_function(key: str, size=100):
    """Take a key as an input and calculate an integer out put
    Output should be between 0 and size
    """
    key = str(key)
    hash_value = 0
    for letter in key:
        hash_value += ASCII_MAPPING[letter]
    hash_value = hash_value % size
    return hash_value


class Dictionary:
    def __init__(self):
        self._capacity = 10
        self._size = 0
        self._storage = []
        self._resize_and_rehash()

    def _resize_and_rehash(self):
        old_storage = self._storage.copy()
        self._capacity *= 2
        self._storage = []
        for _ in range(self._capacity):
            self._storage.append([])

        for cell in old_storage:
            for key, value in cell:
                self._put(key, value)

    def _get(self, search_key):
        index = hash_function(search_key, size=self._capacity)
        for key, value in self._storage[index]:
            if search_key == key:
                return value
        raise KeyError(search_key)

    def _put(self, key, value):
        self._size += 1
        if self._size == self._capacity:
            self._resize_and_rehash()
        index = hash_function(key, size=self._capacity)
        self._storage[index].append((key, value))

    def __getitem__(self, key):
        return self._get(key)

    def __setitem__(self, key, value):
        self._put(key, value)

    def keys(self):
        all_keys = []
        for bucket in self._storage:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys

    def values(self):
        all_values = []
        for bucket in self._storage:
            for _, value in bucket:
                all_values.append(value)
        return all_values

    def items(self):
        all_items = []
        for bucket in self._storage:
            all_items.extend(bucket)
        return all_items

    def __str__(self):
        return f"Dictionary({dict(self.items())})"


demo_dict = Dictionary()
demo_dict["1"] = 1
print(demo_dict["1"])
demo_dict["2"] = 2
demo_dict[(1, 2, 3)] = (1, 2, 3)
print(demo_dict._storage)
