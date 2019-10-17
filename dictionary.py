import hashlib
from linked_list import LinkedList


class Dictionary:

    # 0(1) compared to Linked Lists which are 0(n)

    def set(self, key, value):
        '''
        Adds an item to the dictionary
        :param key: key
        :param value: value
        '''

        item = (key, value)
        index = self.get_index(key)

        if self.data[index] is None:
            self.data[index] = item

        elif isinstance(self.data[index], tuple):
            currentval = self.data[index]
            newlist = LinkedList()

            newlist.insert_front(currentval)
            newlist.insert_front(item)

            self.data[index] = newlist

        else:
            self.data[index].insert_front(item)

    def get(self, key):
        '''
        Gets a value associated with the key.
        :param key: key
        :return: The value of the item located at with the key.
        '''

        index = self.get_index(key)

        if self.data[index] is None:
            return None

        if isinstance(self.data[index], tuple):
            item = self.data[index]
            if item[0] == key:
                return item[1]
            else:
                return None

        elif isinstance(self.data[index], LinkedList):
            ll = self.data[index]
            for i in ll:
                if i.value[0] == key:
                    return i.value[1]

            return None

    def remove(self, key):
        '''
        :param key:
        :return:
        '''
        index = self.get_index(key)

        if self.data[index] is None:
            return None

        elif isinstance(self.data[index], tuple):
            self.data[index] = None

        elif isinstance(self.data[index], LinkedList):
            ll = self.data[index]
            for i in ll:
                if i.value[0] == key:
                    ll.delete_by_value(i.value)
                else:
                    continue

    # def contains(self, key):
    #     '''
    #
    #     :param key:
    #     :return: bool
    #     '''

    def get_index(self, key):
        '''
        
        :return: index
        '''
        index = hash(key) % 10

        return abs(index)

    def __init__(self):
        self.data = [None] * 10

    def __repr__(self):
        return f"Dictionary object with {len(self)} entries."

    def __len__(self):
        '''
        get the length of your dictionary
        :return: int: Total number of items in the Dictionary
        '''

        count = 0

        for i in self.data:

            if i is None:
                continue

            elif isinstance(i, tuple):
                count += 1

            elif isinstance(i, LinkedList):
                numberofitems = len(i)
                count += numberofitems

        return count
