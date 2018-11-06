#!/usr/bin/env python
# -*- coding: utf-8
"""
##################### Q2 Question B - ORMUCO ####################
#-------------------------- Luiz Roma --------------------------#
#
# This code implements a comparison between 2 strings
#
# QUESTION ENUMERATION
# The goal of this question is to write a software library that
# accepts 2 version string as input and returns whether one is
# greater than, equal, or less than the other. As an example:
# “1.2” is greater than “1.1”. Provide all test cases imaginable
#
#---------------------------------------------------------------#
#################################################################
"""

import unittest

class Stringerize(object):
    """
    STRINGERIZE IS A CLASS ENABLING COMPARISON BETWEEN 2 INPUTS
    there are 1 initializer (constructor) and 7 methods
    it simply verifies whether the inputs are strings or numbers
    and enables verification like superior, inferior, comparison
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.type = "none"
        self.initialize()
    """
    CONSTRUCTOR WITH ARGUMENTS "a" AND "b"
    it gives the object the values entered during its creation
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :param type: set the type of the entries as strings or numbers
    """

    def initialize(self):
        if(isinstance(self.a, str) and isinstance(self.b, str)): # are they strings ?
            self.type = "strings"
        elif(isinstance(self.a, float) and isinstance(self.b, float)): # are they integers or floats ?
            self.type = "numbers"
        else:
            self.type = "none"
            raise NameError("wrong type")
    """
    INITIALIZING TYPE OF OBJECT
    it can be "strings", "numbers", "none"
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :param type: set the type of the entries as strings or numbers
    :raise: error when type is not possibly identified
    """

    def check_number_inside(self):
        try:
            float(self.a)
            float(self.b)
            return 1
        except:
            raise NameError("no numbers in strings")
    """
    CHECK IF CONVERTION IS SIMPLE
    it checks whether is there any number inside (is it convertible or not ?)
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :raise: error when there is no number in string received from user
    :return: 1 when there is number
    """

    def convert_to_number(self):
        if(self.type == "numbers"):
            return 1
        elif(self.type == "strings"):
            try:
                self.check_number_inside()
            except:
                raise NameError("strings can not be converted")
            else:
                self.a = float(self.a)
                self.b = float(self.b)
                self.type = "numbers"
                return 1
        else:
            raise NameError("type not accepted")
    """
    CONVERT INPUTS INTO NUMBERS
    it checks the object "type" and converts the inputs in numbers
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :param type: set the type of the entries as strings or numbers
    :raise: error when strings can not be converted to numbers
    :return: 1 when all is good
    """

    def superior(self) -> float:
        if(self.type == "numbers"):
            max_value = max(self.a, self.b)
            min_value = min(self.a, self.b)
            return max_value
        else:
            try:
                self.convert_to_number()
            except:
                raise NameError("strings need to be fixed")
            else:
                return self.superior()
    """
    RETURNS MAX_VALUE
    it returns the maximum value between the 2 inputs
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :param max_value: get the maximum from "a" and "b"
    :param min_value: get the minimum from "a" and "b"
    :raise: error when strings are not yet converted to numbers
    :return: the max value among 2 variables
    """

    def inferior(self) -> float:
        if(self.type == "numbers"):
            max_value = max(self.a, self.b)
            min_value = min(self.a, self.b)
            return min_value
        else:
            try:
                self.convert_to_number()
            except:
                raise NameError("strings need to be fixed")
            else:
                return self.inferior()
    """
    RETURNS MIN_VALUE
    it returns the minimum value between the 2 inputs
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :param type: set the type of the entries as strings or numbers
    :param max_value: get the maximum from "a" and "b"
    :param min_value: get the minimum from "a" and "b"
    :raise: error when strings are not yet converted to numbers
    :raise: error when string are not yet converted to numbers
    :return: the min value among 2 variables
    """

    def print_superior(self):
        return str(self.superior())+" is greater than "+str(self.inferior())
    """
    FROM SUPERIOR, PRINTS THE PHRASE
    it prints the comparison using "greater than" expression
    :return: the string comparing superior (max) and inferior (min) values
    """

    def print_inferior(self):
        return str(self.inferior())+" is less than "+str(self.superior())
    """
    FROM INFERIOR, PRINTS THE PHRASE
    it prints the comparison using "less than" expression
    :return: the string comparing inferior (min) and superior (max) values
    """

    def comparison(self):
        if(self.type == "numbers"):
            if(self.a != self.b):
                return self.print_superior()
            else:
                return "Both numbers are equal"
        else:
            try:
                self.convert_to_number()
            except:
                raise NameError("strings need to be fixed")
            else:
                return self.comparison()
    """
    COMPARE NUMBERS; ARE THEY EQUAL ? DON'T, PRINTS SUPERIOR PHRASE
    it prints the comparison usint "greater than" expression unless the inputs are equal
    :param a: for the 1st string input by user
    :param b: for the 2nd string input by user
    :raise: error when there is a need of convertion
    :return: or numbers are equal or the superior function
    """

class TestStringerize(unittest.TestCase):
    """
    STRINGERIZE UNIT TEST CASE CLASS
    there are some unit tests to verify/check whether the methods and constructor
    are working correctly as built/developped
    """

    def test_input_as_string(self):
        self.x = Stringerize("1.4", "2.0")
        self.assertEqual(self.x.a, "1.4")
        self.assertEqual(self.x.b, "2.0")
    """
    using STRINGS as inputs, it checks it is correctly initializing
    """

    def test_input_as_number(self):
        self.y = Stringerize(1.4, 2.0)
        self.assertEqual(self.y.a, 1.4)
        self.assertEqual(self.y.b, 2.0)
    """
    using NUMBERS as inputs, it checks it is correctly initializing
    """

    def test_input_type_as_string(self):
        self.x = Stringerize("1.4", "2.0")
        self.assertEqual(self.x.type, "strings")
    """
    using STRINGS as inputs, it checks the object "type"
    """

    def test_input_type_as_number(self):
        self.y = Stringerize(1.4, 2.0)
        self.assertEqual(self.y.type, "numbers")
    """
    using NUMBERS as inputs, it checks the object "type
    """

    def test_initialization_as_bool(self):
        with self.assertRaises(NameError):
            self.z = Stringerize(False, True)
    """
    using BOOLEANS as inputs, it checks it is correctly initializing
    """

    def test_initialization_as_bool(self):
        with self.assertRaises(NameError):
            self.z = Stringerize(False, True)
            self.assertEqual(self.z.type, "none")
    """
    using BOOLEANS as inputs, it checks the object "type"
    """

    def test_type_after_conversion_as_strings(self):
        self.x = Stringerize("1.4", "2.0")
        self.x.convert_to_number()
        self.assertEqual(self.x.type, "numbers")
    """
    using STRINGS as inputs and calling convertion method
    it checks the object "type" after convertion
    """

    def test_type_after_conversion_as_numbers(self):
        self.y = Stringerize(1.4, 2.0)
        self.y.convert_to_number()
        self.assertEqual(self.y.type, "numbers")
    """
    using NUMBERS as inputs and calling convertion metdho
    it checks the object "type" after convertion
    """

    def test_conversion_as_strings_works(self):
        self.x = Stringerize("1.4", "2.0")
        self.x.convert_to_number()
        self.assertEqual(self.x.a, 1.4)
        self.assertEqual(self.x.b, 2.0)
    """
    using STRINGS as inputs, it checks whether convertion method works
    """

    def test_conversion_as_numbers_works(self):
        self.y = Stringerize(1.4, 2.0)
        self.y.convert_to_number()
        self.assertEqual(self.y.a, 1.4)
        self.assertEqual(self.y.b, 2.0)
    """
    using NUMBERS as inputs, it checks whether convertion method doesn't affect inputs
    """

    def test_raises_no_number(self):
        self.x = Stringerize("x1.4", "2.0")
        with self.assertRaises(NameError):
            self.x.check_number_inside()
    """
    using STRINGS as inputs, it checks whether convertion method raises an exception
    """

    def test_raises_cant_convert(self):
        self.x = Stringerize("x1.4", "2.0")
        with self.assertRaises(NameError):
            self.x.convert_to_number()
    """
    using STRINGS as inputs, it checks whether convertion method raises an exception
    """

    def test_asserts_max_strings(self):
        self.x = Stringerize("1.4", "2.0")
        self.assertEqual(self.x.superior(), 2.0)
    """
    using STRINGS as inputs, it checks whether superior method returns what is expected
    """

    def test_asserts_min_strings(self):
        self.x = Stringerize("1.4", "2.0")
        self.assertEqual(self.x.inferior(), 1.4)
    """
    using STRINGS as inputs, it checks whether inferior method returns what is expected
    """

    def test_asserts_max_numbers(self):
        self.y = Stringerize(1.4, 2.0)
        self.assertEqual(self.y.superior(), 2.0)
    """
    using NUMBERS as inputs, it checks whether superior method returns what is expected
    """

    def test_asserts_min_numbers(self):
        self.y = Stringerize(1.4, 2.0)
        self.assertEqual(self.y.inferior(), 1.4)
    """
    using NUMBERS as inputs, it checks whether inferior method returns what is expected
    """

    def test_asserts_returns_greater_strings(self):
        self.x = Stringerize("1.4", "2.0")
        self.assertEqual(self.x.print_superior(), "2.0 is greater than 1.4")
    """
    using STRINGS as inputs, it checks whether print_superior method returns what is expected
    """

    def test_asserts_returns_greater_numbers(self):
        self.y = Stringerize(1.4, 2.0)
        self.assertEqual(self.y.print_superior(), "2.0 is greater than 1.4")
    """
    using NUMBERS as inputs, it checks whether print_superior method returns what is expected
    """

    def test_asserts_returns_less_strings(self):
        self.x = Stringerize("1.4", "2.0")
        self.assertEqual(self.x.print_inferior(), "1.4 is less than 2.0")
    """
    using STRINGS as inputs, it checks whether print_inferior method returns what is expected
    """

    def test_asserts_returns_less_numbers(self):
        self.y = Stringerize(1.4, 2.0)
        self.assertEqual(self.y.print_inferior(), "1.4 is less than 2.0")
    """
    using NUMBERS as inputs, it checks whether print_inferior method returns what is expected
    """

    def test_asserts_returns_equal_strings(self):
        self.x = Stringerize("1.4", "1.4")
        self.assertEqual(self.x.comparison(), "Both numbers are equal")
    """
    using STRINGS as inputs, it checks whether comparison method returns what is expected
    """

    def test_asserts_returns_equal_numbers(self):
        self.y = Stringerize(1.4, 1.4)
        self.assertEqual(self.y.comparison(), "Both numbers are equal")
    """
    using NUMBERS as inputs, it checks whether comparison method returns what is expected
    """

    def test_asserts_comparison_sup_strings(self):
        self.x = Stringerize("1.4","2.0")
        self.assertEqual(self.x.comparison(), "2.0 is greater than 1.4")
    """
    using STRINGS as inputs, it checks whether comparison method returns what is expected
    """

    def test_asserts_comparison_sup_numbers(self):
        self.y = Stringerize(1.4,2.0)
        self.assertEqual(self.y.comparison(), "2.0 is greater than 1.4")
    """
    using NUMBERS as inputs, it checks whether comparison method returns what is expected
    """

if __name__ == "__main__":
    unittest.main()
