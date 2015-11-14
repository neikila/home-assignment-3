# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test_calculator import PositiveTestCase, NegativeTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(PositiveTestCase),
        unittest.makeSuite(NegativeTestCase)
        ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
