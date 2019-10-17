from data_structures.exceptions.StackEmptyException import StackEmptyException


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prior = None


class DoublyLinkedList:
    
    def __init__(self):
        self._first = None
        self._last = None

    def insert_front(self, item):
        """
        0(1)
        Insert a node at the front of the DLinkedList
        """
        if self._first is None:
            newnode = Node(item)
            self._first = newnode
            self._last = newnode

        else:
            newnode = Node(item)
            newnode.next = self._first
            self._first.prior = newnode
            self._first = newnode

    def insert_back(self, item):
        '''
        0(n)
        Insert a node at the back of the DLinkedList
        '''
        if self._first is None:
            newnode = Node(item)
            self._last = newnode
            self._first = newnode

        else:
            newnode = Node(item)
            newnode.prior = self._last
            self._last.next = newnode
            self._last = newnode

    def pop_front(self):
        """
        0(n)
        Take a node from the front of the DLinkedList
        :return: value of first node in DLinkedList
        """
        if len(self) == 0:
            raise StackEmptyException("Can't pop an empty LinkedList")

        elif len(self) <= 1:
            node = self._first
            self._first = node.next
            return node.value

        else:
            node = self._first
            self._first = node.next
            self._first.prior = None
            return node.value

    def pop_back(self):
        """
        0(n)
        Take a node from the back of the DLinkedList
        :return: value of last node in DLinkedList
        """
        if len(self) == 0:
            raise StackEmptyException("Can't pop an empty LinkedList")

        elif len(self) <= 1:
            node = self._last
            self._last = node.prior
            return node.value

        else:
            node = self._last
            self._last = node.prior
            self._last.next = None
            return node.value

    def __len__(self):
        """
        0(n)
        Returns the length of the list
        :return: int value of the number of nodes in the dll
        """
        counter = 0
        node = self._first

        while node:
            node = node.next
            counter += 1

        return counter

    def __reversed__(self):
        ...

    def reverse_without_new_dll(self):
        ...

    def delete_from_specific_index(self, index):
        ...

    def pop_from_specific_index(self, index):
        ...