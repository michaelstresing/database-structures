import unittest

from dictionary import Dictionary


class TestStack(unittest.TestCase):

    def can_set_and_get_values(self):
        dic = Dictionary()
        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        val1 = dic.get("Hello")
        val2 = dic.get("Coding")
        val3 = dic.get("Add")

        self.assertEqual("World", val1, "The set or get did not work")
        self.assertEqual("Coding", val2, "The set or get did not work")
        self.assertEqual("Value", val3, "The set or get did not work")

    def can_override_values(self):
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

    def cannot_get_value_doesnt_exist(self):
        dic = Dictionary()
        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        val1 = dic.get("Good Bye")
        val2 = dic.get("coding")    # Lower-case c (not capital)

        self.assertEqual(None, val1, "Getting a value not in the dictionary is broken")
        self.assertEqual(None, val2, "Getting a value not in the dictionary is broken")

    def can_remove_values(self):
        dic = Dictionary()
        dic.set("Hello", "world")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        del dic["Hello"]
        del dic["Coding"]

        val1 = dic.get("Hello")
        val2 = dic.get("Coding")
        val3 = dic.get("Add")

        self.assertEqual(None, val1, "The value remove didn't work")
        self.assertEqual(None, val2, "The value remove didn't work")
        self.assertEqual("Value", val3, "The value remove did something it shouldn't have")

    def cannot_remove_from_empty_dict_value(self):
        dic = Dictionary()
        del dic["Hello"]

        self.assertRaises(TypeError, )

    def can_get_length_of_dic(self):
        dic = Dictionary()
        dic.set("Hello", "World")
        dic.set("Coding", "Is fun")
        dic.set("Add", "Value")

        diclen = len(dic)

        self.assertEqual(3, diclen, "The length counter doesn't work")

    def can_get_length_of_empty_dic(self):
        dic = Dictionary()
        diclen = len(dic)

        self.assertEqual(0, diclen, "The length counter doesn't work")

    def can_correctly_repr_dic(self):
        dic = Dictionary()
        dic.set("Hello", "World")


