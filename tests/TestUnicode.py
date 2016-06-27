# encoding=utf-8
from __future__ import print_function

from six import text_type

__author__ = 'hiepsimu'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = u"Việt Nam"

        print(a.__class__)
        self.assertTrue(isinstance(a, text_type))
        self.assertTrue(isinstance(text_type(a), text_type))

        print(text_type(a).__class__)


if __name__ == '__main__':
    unittest.main()
