import unittest

from dictionary import Dictionary


class TestDict(unittest.TestCase):

    def test_can_set_and_get_values(self):
        dic = Dictionary()

        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        val1 = dic.get("Hello")
        val2 = dic.get("Coding")
        val3 = dic.get("Add")

        self.assertEqual("World", val1, "The set or get did not work")
        self.assertEqual("Is fun", val2, "The set or get did not work")
        self.assertEqual("Value", val3, "The set or get did not work")

    def test_can_override_values(self):
        dic = Dictionary()

        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        dic.set("Hello", "London")
        dic.set("Coding", "Rocks")

        val1 = dic.get("Hello")
        val2 = dic.get("Coding")
        val3 = dic.get("Add")

        self.assertEqual("London", val1, "The overwrite didn't work")
        self.assertEqual("Rocks", val2, "The overwrite didn't work")
        self.assertEqual("Value", val3, "The overwrite did something it shouldn't have")

    def test_cannot_get_value_doesnt_exist(self):
        dic = Dictionary()

        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        val1 = dic.get("Good Bye")
        val2 = dic.get("coding")    # Lower-case c (not capital)

        self.assertEqual(None, val1, "Getting a value not in the dictionary is broken")
        self.assertEqual(None, val2, "Getting a value not in the dictionary is broken")

    def test_can_remove_values(self):
        dic = Dictionary()

        dic.set("Hello", "world")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        dic.remove("Hello")
        dic.remove("Coding")

        val1 = dic.get("Hello")
        val2 = dic.get("Coding")
        val3 = dic.get("Add")

        self.assertEqual(None, val1, "The value remove didn't work")
        self.assertEqual(None, val2, "The value remove didn't work")
        self.assertEqual("Value", val3, "The value remove did something it shouldn't have")

    def test_cannot_remove_from_empty_dict_value(self):
        dic = Dictionary()
        dic.set("Hello", "World")
        dic.set("Bye", "Bali")

        dic.remove("Hello")

        val1 = dic.get("Hello")

        self.assertEqual(None, val1, "Dictionary remove item doesn't work")

    def test_can_get_length_of_dic(self):
        dic = Dictionary()

        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        diclen = len(dic)

        self.assertEqual(3, diclen, "The length counter doesn't work")

    def test_can_get_length_of_empty_dic(self):
        dic = Dictionary()
        diclen = len(dic)

        self.assertEqual(0, diclen, "The length counter doesn't work")

    def test_can_correctly_repr_dic(self):
        dic = Dictionary()
        dic.set("Hello", "World")
        rep = str(dic)

        self.assertEqual("Dictionary object with 1 entries.", rep, "The representation is wrong")
