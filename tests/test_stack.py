import unittest

from stack import Stack
from exceptions.StackEmptyException import StackEmptyException


class TestStack(unittest.TestCase):

    def test_can_push_and_pop_in_right_order(self):

        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        
        pop1 = my_stack.pop()
        pop2 = my_stack.pop()
        
        self.assertEqual(2, pop1, "first pop did not have the expected value")
        self.assertEqual(1, pop2, "second pop did not have the expected value")

    def test_can_peek_in_right_order(self):

        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)

        peek1 = my_stack.peek()
        peek2 = my_stack.peek()

        self.assertEqual(2, peek1, "first peek did not have the expected value")
        self.assertEqual(2, peek2, "second peek did not have the expected value")

    def test_len_correctly_counts(self):

        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)

        length = len(my_stack)

        self.assertEqual(4, length, "The length count works")

    def test_can_count_empty_stack(self):

        my_empty_stack = Stack()
        empty_len = len(my_empty_stack)
        self.assertEqual(0, empty_len, "The length count is all messed (empty test)")

    def test_will_raise_exception_on_empty_stack(self):

        empty = Stack()
        self.assertRaises(StackEmptyException, empty.pop)
        self.assertRaises(StackEmptyException, empty.peek)

    def test_reverse_function(self):

        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        
        reversed(my_stack)

        pop1 = my_stack.pop()
        pop2 = my_stack.pop()
        pop3 = my_stack.pop()

        self.assertEqual(1, pop1, "The Reverse Function is broken")
        self.assertEqual(2, pop2, "The Reverse Function is broken")
        self.assertEqual(3, pop3, "The Reverse Function is broken")
