# encoding=utf-8
__author__ = 'hiepsimu'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = u"Việt Nam"

        print a

        print unicode(a)


if __name__ == '__main__':
    unittest.main()
