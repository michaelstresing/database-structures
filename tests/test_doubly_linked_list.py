import unittest

from doubly_linked_list import DoublyLinkedList
from exceptions.StackEmptyException import StackEmptyException


class TestStack(unittest.TestCase):

    def test_front(self):

        dll = DoublyLinkedList()
        dll.insert_front(9)
        dll.insert_front(2)
        dll.insert_front(3)

        pop1 = dll.pop_front()
        pop2 = dll.pop_front()
        pop3 = dll.pop_front()

        self.assertEqual(3, pop1, "Pop front is broken")
        self.assertEqual(2, pop2, "Pop front is broken ")
        self.assertEqual(9, pop3, "Pop front is broken")

    def test_back(self):

        dll = DoublyLinkedList()
        dll.insert_back(9)
        dll.insert_back(2)
        dll.insert_back(3)

        pop1 = dll.pop_back()
        pop2 = dll.pop_back()
        pop3 = dll.pop_back()

        self.assertEqual(3, pop1, "Pop back is broken")
        self.assertEqual(2, pop2, "Pop back is broken ")
        self.assertEqual(9, pop3, "Pop back is broken")

    def test_queue(self):

        dll = DoublyLinkedList()
        dll.insert_front(9)
        dll.insert_front(2)
        dll.insert_front(3)

        pop1 = dll.pop_back()
        pop2 = dll.pop_back()
        pop3 = dll.pop_back()

        self.assertEqual(9, pop1, "Pop back is broken")
        self.assertEqual(2, pop2, "Pop back is broken ")
        self.assertEqual(3, pop3, "Pop back is broken")

    def test_reverse_queue(self):

        dll = DoublyLinkedList()
        dll.insert_back(9)
        dll.insert_back(2)
        dll.insert_back(3)

        pop1 = dll.pop_front()
        pop2 = dll.pop_front()
        pop3 = dll.pop_front()

        self.assertEqual(9, pop1, "Pop back is broken")
        self.assertEqual(2, pop2, "Pop back is broken ")
        self.assertEqual(3, pop3, "Pop back is broken")

    def test_counter_works(self):

        dll = DoublyLinkedList()
        counter = len(dll)

        self.assertEqual(0, counter, "Counter is broken (0)")

        dll.insert_front(9)
        dll.insert_front(2)
        dll.insert_front(3)

        counter3 = len(dll)

        self.assertEqual(3, counter3, "Counter is broken (After insert)")

        dll.pop_front()
        dll.pop_front()

        counter1 = len(dll)

        self.assertEqual(1, counter1, "Counter is broken (After insert, then pop)")

    def test_raises_exception_for_empty_list(self):

        dll = DoublyLinkedList()
        self.assertRaises(StackEmptyException, dll.pop_front)
