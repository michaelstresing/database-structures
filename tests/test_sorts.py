import unittest
import random
from datastructures_and_algorithms.sorting import quick_sort, bubble_sort, bubble_sort_with_stop, insertion_sort


class TestSorts(unittest.TestCase):

    def test_can_quick_sort(self):

        # Arrange
        test_list = [random.randint(0, 1000) for _ in range(10000)]

        # Act
        testlist = quick_sort(test_list)

        # Assert
        for i in range(len(testlist) - 1):
            self.assertLessEqual(testlist[i], testlist[i + 1], "Its not in order dummy.")

    def test_can_bubble_sort(self):

        # Arrange
        test_list = [random.randint(0, 1000) for _ in range(10000)]

        # Act
        testlist = bubble_sort(test_list)

        # Assert
        for i in range(len(testlist) - 1):
            self.assertLessEqual(testlist[i], testlist[i + 1], "Its not in order dummy.")

    def test_can_bubble_sort_with_stop(self):

        # Arrange
        test_list = [random.randint(0, 1000) for _ in range(10000)]

        # Act
        testlist = bubble_sort_with_stop(test_list)

        # Assert
        for i in range(len(testlist) - 1):
            self.assertLessEqual(testlist[i], testlist[i + 1], "Its not in order dummy.")

    def test_can_insertion_sort(self):

        # Arrange
        test_list = [random.randint(0, 1000) for _ in range(10000)]

        # Act
        testlist = insertion_sort(test_list)

        # Assert
        for i in range(len(testlist) - 1):
            self.assertLessEqual(testlist[i], testlist[i + 1], "Its not in order dummy.")

