class HashMap:
    def __init__(self):
        self.size = 5
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):

                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:

            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        return None


if __name__ == "__main__":
    my_map = HashMap()

    my_map.put("apple", 10)
    my_map.put("banana", 5)
    my_map.put("orange", 15)

    print(my_map.get("apple"))
    print(my_map.get("banana"))
    print(my_map.get("grape"))
    print(my_map.table)
