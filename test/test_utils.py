import unittest

from utils import *


class TestFileUtils(unittest.TestCase):
    def test_file_backup(self):
        file_path = r"E:\test.txt"
        backup = FileUtil.file_backup(file_path)
        self.assertTrue(FileUtil.file_exists(backup))
        self.assertTrue(FileUtil.is_file(backup))

    def test_write_file(self):
        file_path = r"E:\test.txt"
        content = "测试写入文件"
        self.assertTrue(FileUtil.write_file(file_path, content, 'w'))

    def test_file_exists(self):
        file_path = r"E:\test.txt"
        self.assertTrue(FileUtil.file_exists(file_path))

    def test_is_file(self):
        file_path = r"E:\test.txt"
        self.assertTrue(FileUtil.is_file(file_path))

    def test_is_dir(self):
        dir_path = r"E:"
        self.assertTrue(FileUtil.is_dir(dir_path))

    def test_get_file_name(self):
        dir_path = r"E:"
        self.assertTrue(FileUtil.get_file_name(dir_path))

    def test_get_sub_dir(self):
        dir_path = r"E:"
        self.assertTrue(FileUtil.get_sub_dir(dir_path))


class StrUtilTest(unittest.TestCase):
    def test_add_char_to_lines(self):
        original_text = """This is line 1.
This is line 2.
This is line 3."""
        print(original_text)
        result = StrUtil.add_char_to_lines(original_text, 2)
        print(result)
        self.assertEqual(result, "  This is line 1.\n  This is line 2.\n  This is line 3.")


if __name__ == '__main__':
    unittest.main()
