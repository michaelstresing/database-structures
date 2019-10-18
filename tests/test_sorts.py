import unittest
import random
from building_datastructures.sorting import quick_sort, bubble_sort


class TestSorts(unittest.TestCase):

    def test_can_quick_sort(self):

        # Arrange
        test_list = [random.randint(0, 100000) for _ in range(10000)]

        # Act
        testlist = quick_sort(test_list)

        # Assert
        for i in range(len(testlist) - 1):
            self.assertLessEqual(testlist[i], testlist[i + 1], "Its not in order dummy.")

    def test_can_bubble_sort(self):

        # Arrange
        test_list = [random.randint(0, 10) for _ in range(5)]

        # Act
        testlist = bubble_sort(test_list)

        # Assert
        for i in range(len(testlist) - 1):
            self.assertLessEqual(testlist[i], testlist[i + 1], "Its not in order dummy.")
