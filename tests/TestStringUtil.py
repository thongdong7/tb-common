from tb_common.utils.string_util import substring_by_space

__author__ = 'hiepsimu'

import unittest


class StringUtilTestCase(unittest.TestCase):
    def test_substring_by_space(self):
        text = 'hello world'
        ret = substring_by_space(text, 8)
        self.assertEqual('hello', ret)


if __name__ == '__main__':
    unittest.main()
