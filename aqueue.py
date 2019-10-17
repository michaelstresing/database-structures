from exceptions.StackEmptyException import StackEmptyException


class AQueue:   # Named with A as class/file names Queue/queue.py caused some issues with the debugger.
    
    def __init__(self):
        self._data = list()
    
    def enqueue(self, item):
        """
        0(1)
        Adds item to the queue
        """
        self._data.append(item)
            
    def dequeue(self):
        """
        0(1) [was 0(n) when used if/else, rather than try/except]
        Remove item from the queue.
        :return: The oldest(bottom) item in the queue
        """
        try:
            item = self._data[0]
            del self._data[0]
            return item

        except():
            raise StackEmptyException("The Queue is empty")
    
    def __len__(self):
        """
        0(n)
        Returns the length of the queue
        :return: int length of the items in the list
        """
        return len(self._data)

    def __reversed__(self):
        """
        0(n)
        Reverses the items in the Stack
        :return: New Stack, reversed order from original
        """

        newqueue = self._data[::-1]
        self._data = newqueue
