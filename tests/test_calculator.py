# -*- coding: utf-8 -*-

from unittest import TestCase, TestLoader, TextTestRunner
from calc import calculate

class PositiveTestCase(TestCase):
    def setUp(self):
        # Nothing to do here
        pass

    def tearDown(self):
        # Nothing to do here
        pass

# Multiply
    def test_multiply(self):
        args = (7, 2)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 14)

    def test_multiply_another_arguments_order(self):
        args = (2, 7)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 14)

    def test_multiply_negative_argument(self):
        args = (2, 7)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 14)

    def test_double_multiply_resultx2(self):
        args = (2, 7.3)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 14.6)

    def test_mul_point_error(self):
        args = (12, 0.1)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 1.2)


# Sum
    def test_sum(self):
        args = (2, 7)
        operation = 'x+y'
        self.assertEqual(calculate(args, operation), 9)

    def test_sum_point_error(self):
        args = (0.2, 0.1)
        operation = 'x+y'
        self.assertEqual(calculate(args, operation), 0.3)

    def test_sum_another_arguments_order(self):
        args = (7, 2)
        operation = 'x+y'
        self.assertEqual(calculate(args, operation), 9)

    def test_sum_negative_argument(self):
        args = (7, -2)
        operation = 'x+y'
        self.assertEqual(calculate(args, operation), 5)

    def test_sum_argument_is_negative(self):
        args = (-7, 2)
        operation = 'x+y'
        self.assertEqual(calculate(args, operation), -5)


# Division
    def test_division(self):
        args = (14, 2)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 7)

    def test_double_division_result(self):
        args = (7, 2)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 3.5)

    def test_division_negative_argument(self):
        args = (14, -2)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), -7)

    def test_division_another_argument_is_negative(self):
        args = (-14, 2)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), -7)

    def test_division_pointer_error(self):
        args = (0.3, 0.1)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 3)


# Sub
    def test_sub(self):
        args = (2, 7)
        operation = 'x-y'
        self.assertEqual(calculate(args, operation), -5)

    def test_sub_negative_argument(self):
        args = (7, -2)
        operation = 'x-y'
        self.assertEqual(calculate(args, operation), 9)

    def test_sub_argument_is_negative(self):
        args = (-7, 2)
        operation = 'x-y'
        self.assertEqual(calculate(args, operation), -9)

    def test_sub_pointer_error(self):
        args = (0.3, 0.1)
        operation = 'x-y'
        self.assertEqual(calculate(args, operation), 0.2)


# Abs
    def test_abs_positive(self):
        args = 7
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 7)

    def test_abs_positive_float(self):
        args = 0.001
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 0.001)

    def test_abs_negative_argument(self):
        args = -7
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 7)

    def test_abs_negative_argument_float(self):
        args = -0.001
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 0.001)

    def test_abs_zero(self):
        args = 0
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 0)

class NegativeTestCase(TestCase):
    def setUp(self):
        # Nothing to do here
        pass

    def tearDown(self):
        # Nothing to do here
        pass

    def test_division_to_zero(self):
        args = (1, 0)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 'Error: Division to zero is prohibited')

    def test_wrong_operation(self):
        args = (2, 1)
        operation = 'div1'
        self.assertEqual(calculate(args, operation), 'Error: Wrong operation')

    def test_mul_None_first_argument(self):
        args = (None, 1)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')

    def test_mul_None_second_argument(self):
        args = (2, None)
        operation = 'x*y'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')

    def test_div_string_first_argument(self):
        args = ('asd', 1)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')

    def test_div_string_second_argument(self):
        args = (2, 'asd')
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')

    def test_not_num_abs(self):
        args = 'asd'
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')

    def test_not_enough_arguments(self):
        args = (1,)
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 'Error: Not enough arguments')

    def test_no_arguments(self):
        args = ()
        operation = 'x/y'
        self.assertEqual(calculate(args, operation), 'Error: Not enough arguments')

    def test_too_many_arguments(self):
        args = (-1, 1)
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')

    def test_none_argument_in_abs(self):
        args = None
        operation = '|x|'
        self.assertEqual(calculate(args, operation), 'Error: Wrong input argument type')
