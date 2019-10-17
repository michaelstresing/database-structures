import unittest

from data_structures.linked_list import LinkedList
from data_structures.exceptions.StackEmptyException import StackEmptyException


class TestStack(unittest.TestCase):

    def test_insert_pop_correct_order(self):

        ll = LinkedList()
        ll.insert_front(9)
        ll.insert_front(2)
        ll.insert_front(3)

        pop1 = ll.pop_front()
        pop2 = ll.pop_front()
        pop3 = ll.pop_front()

        self.assertEqual(3, pop1, "Pop front is broken")
        self.assertEqual(2, pop2, "Pop front is broken ")
        self.assertEqual(9, pop3, "Pop front is broken")

    def test_counter_works(self):

        ll = LinkedList()
        counter = len(ll)

        self.assertEqual(0, counter, "Counter is broken (0)")

        ll.insert_front(1)
        counter1 = len(ll)

        self.assertEqual(1, counter1, "Counter is broken (1)")

        ll.insert_front(9)
        ll.insert_front(2)
        ll.insert_front(3)
        counter4 = len(ll)

        self.assertEqual(4, counter4, "Counter is broken (After insert)")

        ll.pop_front()
        ll.pop_front()
        counter2 = len(ll)

        self.assertEqual(2, counter2, "Counter is broken (After insert, then pop)")

    def test_raises_exception_for_empty_list(self):

        ll = LinkedList()
        self.assertRaises(StackEmptyException, ll.pop_front)

    def test_reverse_linked_list(self):

        ll = LinkedList()
        ll.insert_front(1)
        ll.insert_front(2)
        ll.insert_front(3)

        ll = reversed(ll)

        pop1 = ll.pop_front()
        pop2 = ll.pop_front()
        pop3 = ll.pop_front()

        self.assertEqual(1, pop1, "Pop front is broken")
        self.assertEqual(2, pop2, "Pop front is broken ")
        self.assertEqual(3, pop3, "Pop front is broken")

    def test_deletes_correct_item(self):

        ll = LinkedList()
        ll.insert_front(1)
        ll.insert_front(2)
        ll.insert_front(3)
        ll.insert_front(4)
        ll.insert_front(5)
        ll.insert_front(6)

        ll.delete_specific(3)

        pop1 = ll.pop_front()
        pop2 = ll.pop_front()
        pop3 = ll.pop_front()
        pop4 = ll.pop_front()
        pop5 = ll.pop_front()

        self.assertEqual(1, pop5, "The item 3 wasn't deleted")
        self.assertEqual(2, pop4, "The item 3 wasn't deleted")
        self.assertEqual(4, pop3, "The item 3 wasn't deleted")
        self.assertEqual(5, pop2, "The item 3 wasn't deleted")
        self.assertEqual(6, pop1, "The item 3 wasn't deleted")

    def test_reverse_linked_list_without_second_list(self):

        ll = LinkedList()
        ll.insert_front(1)
        ll.insert_front(2)
        ll.insert_front(3)

        ll.reverse_within_ll()

        pop1 = ll.pop_front()
        pop2 = ll.pop_front()
        pop3 = ll.pop_front()

        self.assertEqual(1, pop1, "Pop front is broken")
        self.assertEqual(2, pop2, "Pop front is broken ")
        self.assertEqual(3, pop3, "Pop front is broken ")

