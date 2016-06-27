# encoding=utf-8
from tb_common.utils.vietnamese import generate_text_link, to_dungsan

__author__ = 'hiepsimu'

import unittest


class VietnameseTestCase(unittest.TestCase):
    def test_01(self):
        testcases = [
            (u'Tiếng Việt -- _ + [ ] !@%#$%@%^#^%&$&^%*&(^*()&(**  có dấu đây 123', 'Tieng-Viet-co-dau-day-123')
        ]
        for text, expected_result in testcases:
            result = generate_text_link(text)
            self.assertEqual(expected_result, result)

    def test_tohop_dungsan(self):
        text = u"'á''à''ả''ã''ạ''ă''ắ''ằ''ẳ''ẵ''ặ''â''ấ''ầ''ẩ''ẫ''ậ''ú''ù''ủ''ũ''ụ''ư''ứ''ừ''ử''ữ''ự''í''ì''ỉ''ĩ''ị''ó''ò''ỏ''õ''ọ''ô''ố''ồ''ổ''ỗ''ộ''ơ''ớ''ờ''ở''ỡ''ợ''đ''Đ''ý''ỳ''ỷ''ỹ''ỵ''Á''À''Ả''Ã''Ạ''Ă''Ắ''Ẳ''Ẵ''Ặ''Â''Ấ''Ẩ''Ẫ''Ậ''É''È''Ẻ''Ẽ''Ẹ''Ế''Ề''Ể''Ễ''Ệ''Ú''Ù''Ủ''Ũ''Ụ''Ư''Ứ''Ừ''Ử''Ữ''Ự''Í''Ì''Ỉ''Ĩ''Ị''Ó''Ò''Ỏ''Õ''Ọ''Ô''Ố''Ổ''Ỗ''Ộ''Ơ''Ớ''Ờ''Ở''Ỡ''Ợ''Ý''Ỳ''Ỷ''Ỹ''Ỵ'"
        print text
        print to_dungsan(text)

if __name__ == '__main__':
    unittest.main()
