from collections import defaultdict

class MyHashSet:

    def __init__(self):
        self.hash_value = 200
        self.hash_dict = defaultdict(list)

    def add(self, key: int) -> None:

        dict_offset = key % self.hash_value

        if key not in self.hash_dict[dict_offset]:
            self.hash_dict[dict_offset].append(key)
        

    def remove(self, key: int) -> None:
        dict_offset = key % self.hash_value

        if key in self.hash_dict[dict_offset]:
            self.hash_dict[dict_offset].remove(key)
        

    def contains(self, key: int) -> bool:
        dict_offset = key % self.hash_value
        return key in self.hash_dict[dict_offset]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)