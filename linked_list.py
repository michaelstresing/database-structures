from building_datastructures.exceptions.StackEmptyException import StackEmptyException


class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:

    def __init__(self):
        self._head = None

    def __repr__(self):
        current = self._head
        result = []
        while current:
            result.append(f'{current}')
            current = current.next
        return ' -> '.join(result)

    def __reversed__(self):
        newll = LinkedList()
        if len(self) <= 1:
            raise StackEmptyException("You can't reverse an empty or single node LinkedList")
        node = self._head
        while node:
            newll.insert_front(node.value)
            node = node.next
        return newll

    def __len__(self):
        node = self._head
        if self._head is None:
            return 0
        elif self._head.next is None:
            return 1
        else:
            counter = 1
            while node.next:
                counter += 1
                node = node.next
            return counter

    def __iter__(self):
        current = self._head
        for i in range(len(self)):
            yield current
            if current.next is not None:
                current = current.next

    def insert_front(self, item):
        """
        0(1)
        Inserts node at the front of the queue
        """
        self._head = Node(value=item, next=self._head)

    def pop_front(self):
        """
        0(1)
        Removes a node from the front
        :return: The value of the front/top node
        """
        node = self._head

        if node is None:
            raise StackEmptyException("Can't pop an empty LinkedList")

        if node.next is None:
            popnode = self._head
            self._head = None
            return popnode.value

        else:
            popnode = self._head
            self._head = popnode.next
            return popnode.value

    def reverse_within_ll(self):
        """
        0(n)
        Reverses the nodes, without creating a new LinkedList
        """
        nodesize = len(self)

        if nodesize == 0:
            return None

        priornode = self._head
        currentnode = priornode.next
        nextnode = currentnode.next

        priornode.next = None

        while nextnode is not None:
            currentnode.next = priornode

            priornode = currentnode
            currentnode = nextnode
            nextnode = nextnode.next

        self._head = currentnode
        currentnode.next = priornode

    def delete_specific(self, item):
        '''
        0(n)
        Deletes a specific item in the list based on it's place in the list
        :param item: The node place you wish to delete
        '''
        if item not in range(len(self)):
            raise Exception("Item is out of the range")
        else:
            priordelete = None
            placenode = self._head
            postdelete = self._head.next
            counter = 0

            while counter != item:
                priordelete = placenode
                todelete = placenode.next
                postdelete = todelete.next
                placenode = placenode.next
                counter += 1

            priordelete.next = postdelete

    def delete_by_value(self, val):
        """
        0(n)
        Removes the first node from the LinkedList with the given value
        :param val: The value of the node to be deleted
        """

        current = self._head
        previous = None

        while current and current.value != val:
            previous = current
            current = current.next

        if current is None:
            return

        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next
