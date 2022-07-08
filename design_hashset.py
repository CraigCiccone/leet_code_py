# EASY
#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
#
# Example 1:
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet()
# myHashSet.add(1)      // set = [1]
# myHashSet.add(2)      // set = [1, 2]
# myHashSet.contains(1) // return True
# myHashSet.contains(3) // return False, (not found)
# myHashSet.add(2)      // set = [1, 2]
# myHashSet.contains(2) // return True
# myHashSet.remove(2)   // set = [1]
# myHashSet.contains(2) // return False, (already removed)
#
# Constraints:
#
# 0 <= key <= 10^6
# At most 104 calls will be made to add, remove, and contains.


class MyHashSet:
    def __init__(self):
        self.data = [False] * int(1e6 + 1)

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


if __name__ == "__main__":
    my_hash_set = MyHashSet()
    my_hash_set.add(1)  # set = [1]
    my_hash_set.add(2)  # set = [1, 2]
    print(my_hash_set.contains(1))  # return True
    print(my_hash_set.contains(3))  # return False, (not found)
    my_hash_set.add(2)  # set = [1, 2]
    print(my_hash_set.contains(2))  # return True
    my_hash_set.remove(2)  # set = [1]
    print(my_hash_set.contains(2))  # return False, (already removed)
