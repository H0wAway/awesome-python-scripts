import sys
import unittest

import markdown_parse

sys.path.append('..')


class TestURLQuoto(unittest.TestCase):
    def test_url_quoto(self):
        test_urls = [
            (
                r"C:\Users\haowei\Pictures\icon\20 测试.png",
                r"C:/Users/haowei/Pictures/icon/20%20%E6%B5%8B%E8%AF%95.png"),
            (r"..\Pictures\icon\20 测试.png", r"../Pictures/icon/20%20%E6%B5%8B%E8%AF%95.png"),
            (r"..%5CPictures%5Cicon%5C20 测试.png", r"../Pictures/icon/20%20%E6%B5%8B%E8%AF%95.png"),
            (r"../Pictures/icon/20 测试.png", r"../Pictures/icon/20%20%E6%B5%8B%E8%AF%95.png"),
            (
                r"C:/Users/haowei/Pictures/icon/20 测试.png",
                r"C:/Users/haowei/Pictures/icon/20%20%E6%B5%8B%E8%AF%95.png"),
            (r"../Pictures/Screenshots/%E9%92%9D%E6%84%9F%E5%8A%9B%202024-02-04%20160330.png",
             r"../Pictures/Screenshots/%E9%92%9D%E6%84%9F%E5%8A%9B%202024-02-04%20160330.png"),
            (r"..%2FPictures%2FScreenshots%2F%E9%92%9D%E6%84%9F%E5%8A%9B%202024-02-04%20160330.png",
             r"../Pictures/Screenshots/%E9%92%9D%E6%84%9F%E5%8A%9B%202024-02-04%20160330.png")
        ]
        for input_url, expected_url in test_urls:
            # 使用 subTest() 方法，可以在测试用例失败时，输出每个子测试用例的输入参数，且不影响其他测试用例的执行
            with self.subTest(input_url=input_url):
                self.assertEqual(markdown_parse.url_quoto(input_url), expected_url)


class TestImageRegex(unittest.TestCase):
    def test_find_image_matches(self):
        test_contents = r"""1. ![图片](http://example.com/image.png)
                            1. ![图()片](http://example.com/image.png) 123
                            1. ![图[]片](http://example![](.com/image.png)
                            看上去相似但匹配不到的例子：                             123
                            1. [这是一个链接](http://example.com)
                            2. ![图片](http://example.com/im()age.png "图片标题")
                            3. ! [图片](http://example.com/image.png "图片标题")
                            4. !1[图片](http://example.com/image.png "图片标题")
                            5. ![图片]1(http://exa(123)png "图片标题")   ![](123)"""
        matches = markdown_parse.find_image_matches(test_contents)
        count = 0
        for match in matches:
            print("{:<60} {:<50} {:<50}".format(match.group(0), match.group(1), match.group(2)))
            count = count + 1
        print(count)
        self.assertEqual(count, 5)


if __name__ == '__main__':
    unittest.main()
