from exceptions.StackEmptyException import StackEmptyException


class Stack:

    def __init__(self):
        self._data = list()

    def push(self, item):
        """
        0(1)
        Adds an item to the Stack
        :param item: The value of the item wished to be added to the stack.
        :return: Nothing
        """
        self._data.append(item)

    def pop(self):
        """
        0(n) - due to len (could use try/except block for 0(1) instead
        Takes top item on stack off the stack.
        :return: top list item in Stack
        """
        if len(self) < 1:
            raise StackEmptyException("Can't pop an empty stack")
        item = self._data[-1]
        del self._data[-1]

        return item

    def peek(self):
        """
        0(n) - same as above
        Takes the top item on the stack, without deleting it
        :return: top list item in Stack
        """
        if len(self) < 1:
            raise StackEmptyException("Can't peek an empty stack")
        item = self._data[-1]

        return item
        
    def __len__(self):
        """
        0(n)
        Provides the length of Stack as the length of the list() in self._data
        :return: int length
        """

        return len(self._data)

    def __reversed__(self):
        """
        0(n)
        Reverses the items in the Stack
        :return: New Stack, reversed order from original
        """

        newlist = self._data[::-1]
        self._data = newlist