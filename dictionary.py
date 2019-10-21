import hashlib
from datastructures_and_algorithms.linked_list import LinkedList


class Dictionary:

    def __init__(self, size):
        self._data = [None] * size
        self._size = size

    def __repr__(self):
        return f"Dictionary object of {self._size} spaces, with {len(self)} entries."

    def __len__(self):
        count = 0
        for i in self._data:
            if i is None:
                continue
            elif isinstance(i, tuple):
                count += 1
            elif isinstance(i, LinkedList):
                numberofitems = len(i)
                count += numberofitems
        return count

    def set(self, key, value):
        """
        Adds an item to the dictionary
        :param key: key
        :param value: value
        TODO: insert a check to run the expander
        """

        item = (key, value)
        index = self.get_index(key)

        if self._data[index] is None:
            self._data[index] = item

        elif isinstance(self._data[index], tuple):
            currentval = self._data[index]
            newlist = LinkedList()

            newlist.insert_front(currentval)
            newlist.insert_front(item)

            self._data[index] = newlist

        else:
            self._data[index].insert_front(item)

    def get(self, key):
        """
        Gets a value associated with the key.
        :param key: key
        :return: The value of the item located at with the key.
        """

        index = self.get_index(key)

        if self._data[index] is None:
            return None

        if isinstance(self._data[index], tuple):
            item = self._data[index]
            if item[0] == key:
                return item[1]
            else:
                return None

        elif isinstance(self._data[index], LinkedList):
            ll = self._data[index]
            for i in ll:
                if i[0] == key:
                    return i[1]

            return None

    def remove(self, key):
        """
        Remove a key, value pair based on the key
        :param: key
        """

        index = self.get_index(key)

        if self._data[index] is None:
            return None

        elif isinstance(self._data[index], tuple):
            self._data[index] = None

        elif isinstance(self._data[index], LinkedList):
            ll = self._data[index]
            for i in ll:
                if i[0] == key:
                    ll.delete_by_value(i)
                else:
                    continue

    def contains(self, key):
        """
        Check if a dictionary contains something for a given key
        :param: key
        :return: True/False
        """

        index = self.get_index(key)

        if self._data[index] is None:
            return False

        if isinstance(self._data[index], tuple):
            item = self._data[index]
            if item[0] == key:
                return True
            else:
                return False

        elif isinstance(self._data[index], LinkedList):
            ll = self._data[index]
            for i in ll:
                if i.value[0] == key:
                    return True

            return False

    def get_index(self, key):
        """
        Hashes a key and returns an index
        :return: index
        """
        index = hash(key) % self._size

        return abs(index)

    def expand(self):
        """
        Expands the length of the dictionary index array.
        """
        ...
