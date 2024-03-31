import os
import shutil


class MathUtil:
    """工具类简单示例"""

    @staticmethod
    def add(a, b):
        return a + b


class StrUtil:
    """字符串工具类"""

    @staticmethod
    def reverse(s):
        """字符串反转
        Example:
            1. reverse("hello") -> "olleh"
            2. 通过s == s[::-1]判断字符串是否为回文palindrome
        """
        return s[::-1]

    @staticmethod
    def to_upper(s):
        return s.upper()

    @staticmethod
    def add_char_to_lines(str_: str, num: int, char: str = " ", eol: str = "\n"):
        """字符串每行开头添加指定数量的字符
        :param str_: 输入字符串
        :param num: 添加的字符数量
        :param char: 添加的字符，默认为空格
        :param eol: 行结束符，默认为"\n"
        """
        lines = str_.split(eol)  # 按行分割字符串
        indented_lines = []  # 用于存储添加空格后的行
        for i, line in enumerate(lines):
            indented_line = char * num + line  # 在每行前面添加指定数量的空格
            indented_lines.append(indented_line)
        return eol.join(indented_lines)  # 将处理后的行重新组合成字符串


class FileUtil:
    """文件操作工具类
    注意：
        文件路径分隔符一般为"/", Windows系统中也可以用反斜杠"\", 反斜杠在程序中需要转义"\\"
        "./"：代表目前所在的目录
        "../"：代表上一层目录
        在python中，r"字符串"表示原始字符串，不需要对字符串中的特殊字符进行转义
    """

    @staticmethod
    def file_name_handler(file_path_: str) -> tuple[str, str, str, str]:
        """
        根据文件路径获取：
            1. 文件所在目录
            2. 文件名
            3. 文件名（不含扩展名）
            4. 文件扩展名，若 file_path_ 没带扩展名，则返回空字符串
        :returns: (directory, basename, filename, extension)
        """
        # 获取文件的绝对路径
        abs_path = os.path.abspath(file_path_)
        # 规范化处理文件路径，消除路径中的双斜杠、多余的斜杠、点号等
        file_path_ = os.path.normpath(abs_path)
        # 获取文件所在目录
        directory = os.path.dirname(file_path_)
        # 获取文件名
        basename = os.path.basename(file_path_)
        # 获取文件名（不含扩展名）
        filename = os.path.splitext(basename)[0]
        # 获取文件扩展名
        extension = os.path.splitext(basename)[1]
        return directory, basename, filename, extension

    @staticmethod
    def path_change_extension(file_path_: str, new_extension_: str) -> str:
        """
        获取文件修改扩展名后的路径
        :param file_path_: 文件路径
        :param new_extension_: 新的扩展名
        :return: 修改后的文件路径
        """
        file_name_tuple = FileUtil.file_name_handler(file_path_)
        new_file_path = file_name_tuple[0] + '\\' + file_name_tuple[2] + '.' + new_extension_
        # os.rename(file_path_, new_file_path)
        return new_file_path

    @staticmethod
    def file_backup(file_path_: str) -> str:
        """
        将文件原地备份
        :param file_path_: 文件路径
        :return: 备份文件路径
        """
        file_name_tuple = FileUtil.file_name_handler(file_path_)
        backup = file_name_tuple[0] + '\\' + file_name_tuple[2] + '_temp' + file_name_tuple[3]
        shutil.copy(file_path_, backup)
        return backup

    @staticmethod
    def write_file(file_path_: str, content_: str, mode_: str = 'a') -> bool:
        """
        根据输入参数重写或续写文件
        :param file_path_: 文件路径
        :param content_: 写入的内容
        :param mode_: 写入模式，'w'表示重写文件，'a'表示续写文件，默认为续写。文件不存在时都会创建文件
        :return: 写入成功返回True，否则返回False
        """
        # mode_不为w和a是抛出异常
        try:
            if mode_ not in ['w', 'a']:
                raise ValueError("The file writing method must be 'w' or 'a'")
            with open(file_path_, mode_, encoding='utf-8') as file:
                file.write(content_)
            return True
        except Exception as e:
            print("发生错误：", e)
            return False

    @staticmethod
    def file_exists(file_path):
        """检查文件是否存在"""
        return os.path.exists(file_path)

    @staticmethod
    def is_file(file_path):
        """检查路径是否为文件"""
        return os.path.isfile(file_path)

    @staticmethod
    def is_dir(dir_path):
        """检查路径是否为目录"""
        return os.path.isdir(dir_path)

    @staticmethod
    def get_file_name(dictionary_path_: str) -> list[str]:
        """
        获取指定目录下所有的文件名
        """
        list_ = []
        for filename in os.listdir(dictionary_path_):
            if FileUtil.is_file(os.path.join(dictionary_path_, filename)):
                list_.append(filename)
        return list_

    @staticmethod
    def get_sub_dir(dictionary_path_: str) -> list[str]:
        """
        获取指定目录下的子文件夹
        """
        list_ = []
        for filename in os.listdir(dictionary_path_):
            if FileUtil.is_dir(os.path.join(dictionary_path_, filename)):
                list_.append(filename)
        return list_
