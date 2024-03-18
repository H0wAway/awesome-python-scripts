import file_utils
import unittest


class TestFileUtils(unittest.TestCase):
    def test_file_backup(self):
        file_path = r"E:\test.txt"
        backup = file_utils.file_backup(file_path)
        self.assertTrue(file_utils.file_exists(backup))
        self.assertTrue(file_utils.is_file(backup))

    def test_write_file(self):
        file_path = r"E:\test.txt"
        content = "测试写入文件"
        self.assertTrue(file_utils.write_file(file_path, content, 'w'))

    def test_file_exists(self):
        file_path = r"E:\test.txt"
        self.assertTrue(file_utils.file_exists(file_path))

    def test_is_file(self):
        file_path = r"E:\test.txt"
        self.assertTrue(file_utils.is_file(file_path))

    def test_is_dir(self):
        dir_path = r"E:"
        self.assertTrue(file_utils.is_dir(dir_path))

    def test_get_file_name(self):
        dir_path = r"E:"
        self.assertTrue(file_utils.get_file_name(dir_path))

    def test_get_sub_dir(self):
        dir_path = r"E:"
        self.assertTrue(file_utils.get_sub_dir(dir_path))


if __name__ == '__main__':
    unittest.main()
