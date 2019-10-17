from stack import Stack


class BQueue:  # Queue only using two stacks

    def __init__(self):
        self.stackone = Stack()
        self.stacktwo = Stack()

    def enqueue(self, item):
        """
        0(n^2) - worst case, assuming a roughly 50/50 enqueue dequeue rate
        Adds item to the queue
        """

        while len(self.stacktwo) > 0:
            self.stackone.push(self.stacktwo.pop())
        self.stackone.push(item)

    def dequeue(self):
        """
        0(n^2) - worst case, assuming a roughly 50/50 enqueue dequeue rate
        Remove item from the queue.
        :return: The oldest(bottom) item in the queue
        """

        while len(self.stackone) > 0:
            self.stacktwo.push(self.stackone.pop())
        return self.stacktwo.pop()
