import unittest

from bqueue import BQueue
from exceptions.StackEmptyException import StackEmptyException


class TestStack(unittest.TestCase):

    def test_enqueue_dequeue_right_order(self):
        my_queue = BQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        my_queue.enqueue(4)

        deq1 = my_queue.dequeue()
        deq2 = my_queue.dequeue()
        deq3 = my_queue.dequeue()
        deq4 = my_queue.dequeue()

        self.assertEqual(1, deq1, "first pop did not have the expected value")
        self.assertEqual(2, deq2, "second pop did not have the expected value")
        self.assertEqual(3, deq3, "first pop did not have the expected value")
        self.assertEqual(4, deq4, "second pop did not have the expected value")

    def test_len_count_accurate(self):
        my_queue = BQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        my_queue.enqueue(4)

        length = len(my_queue)

        self.assertEqual(4, length, "The length count is all messed")

    def test_still_works_on_empty_queue(self):

        my_empty_queue = BQueue()
        empty_len = len(my_empty_queue)
        self.assertEqual(0, empty_len, "The length count is all messed (empty test)")

    def test_asserts_correctly_on_empty_pop(self):

        empty = BQueue()
        self.assertRaises(StackEmptyException, empty.dequeue)

    # test that it doesn't take more than it has

    def test_reverse_function(self):
        my_q = BQueue()
        my_q.enqueue(1)
        my_q.enqueue(2)
        my_q.enqueue(3)

        reversed(my_q)

        d1 = my_q.dequeue()
        d2 = my_q.dequeue()
        d3 = my_q.dequeue()

        self.assertEqual(3, d1, "The Reverse Function is broken")
        self.assertEqual(2, d2, "The Reverse Function is broken")
        self.assertEqual(1, d3, "The Reverse Function is broken")
