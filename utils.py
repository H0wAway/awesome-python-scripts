import os
import shutil
import time


def time_it(func):
    """计时装饰器
    e.g.
    @time_it
    def func():
        pass
    :returns: 执行func函数的时间
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration_ = time.time() - start_time
        print(f"{func.__name__}: {duration_:.6f} seconds")
        return result

    return wrapper


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
    def add_char_to_lines(str_: str, num: int, char: str = " ", eol: str = "\n") -> str:
        """字符串每行开头添加指定数量的字符
        :param str_: 输入字符串
        :param num: 添加的字符数量
        :param char: 添加的字符，默认为空格
        :param eol: 行结束符，默认为"\n"
        """
        lines = str_.split(eol)  # 按行分割字符串
        indented_lines = []  # 用于存储添加空格后的行
        for i, line in enumerate(lines):
            indented_line = char * num + line  # 在每行前面添加指定数量的字符
            indented_lines.append(indented_line)
        # join方法可以将一个序列（例如列表、元组等）中的字符串按照指定分隔符连接成一个新的字符串
        return eol.join(indented_lines)  # 使用eol连接indented_lines

    @staticmethod
    def format_multiline_output(rows, column_widths):
        """按表格形式打印多行多列字符串
        :param rows: 二维字符串列表
        :param column_widths: 每列的宽度列表
        """
        formatted_rows = []
        for row in rows:
            formatted_row = []
            for i, cell in enumerate(row):
                formatted_row.append("{:<{width}}".format(cell, width=column_widths[i]))
            formatted_rows.append(" ".join(formatted_row))
        return "\n".join(formatted_rows)

    @staticmethod
    def format_single_line_output(row, column_widths):
        """按表格形式打印单行字符串
        :param row: 字符串列表
        :param column_widths: 每列的宽度列表
        """
        formatted_row = []
        for i, cell in enumerate(row):
            formatted_row.append("{:<{width}}".format(cell, width=column_widths[i]))
        return " ".join(formatted_row)


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
        if not os.path.exists(file_path):
            return False
        return os.path.isfile(file_path)

    @staticmethod
    def is_dir(dir_path):
        """检查路径是否为目录"""
        if not os.path.exists(dir_path):
            return False
        return os.path.isdir(dir_path)

    @staticmethod
    def get_sub_name(file_path_: str) -> list[str]:
        """
        获取指定目录下的所有文件和文件夹的名称
        :param file_path_: 目录的路径
        """
        return os.listdir(file_path_)

    @staticmethod
    def get_file_name(dictionary_path_: str) -> list[str]:
        """
        获取指定目录下所有的文件的文件名
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

    @staticmethod
    def delete(file_path_: str) -> bool:
        """
        删除文件或目录
        :param file_path_: 文件路径
        :return: 删除成功返回True，否则返回False
        """
        try:
            # 判断文件是否存在
            if not FileUtil.file_exists(file_path_):
                print("文件不存在")
                return False
            if FileUtil.is_file(file_path_):
                os.remove(file_path_)
            elif FileUtil.is_dir(file_path_):
                shutil.rmtree(file_path_)
            return True
        except Exception as e:
            print("发生错误：", e)
            return False

    @staticmethod
    def get_current_dir():
        """获取当前工作目录"""
        return os.getcwd()

    @staticmethod
    def get_platform():
        """
        获取操作系统名称
        :return: Windows返回'nt'，Linux返回'posix'
        """
        return os.name

    @staticmethod
    def get_separator():
        """获取系统分隔符
        :return: Windows返回'\\'，Linux返回'/', Mac返回':'
        """
        return os.sep

    @staticmethod
    def get_dir_size_recursive(path):
        """递归获取文件夹大小，单位：Bytes"""

        def _get_dir_size_recursive(dir_path_):
            """子函数，方便装饰器调用主函数"""
            try:
                name_list = os.listdir(dir_path_)
            except PermissionError:
                return 0  # 跳过权限不足的目录
            size = 0
            for i in name_list:
                j = f'{dir_path_}/{i}'  # 文件和路径拼接用字符串拼接比.join(path,i)方法更直接更高效
                if os.path.isdir(j):
                    try:
                        size += _get_dir_size_recursive(j)  # 如果是文件，累加文件大小
                    except PermissionError:
                        pass  # 跳过权限不足的文件
                else:
                    size += os.path.getsize(j)
            return size

        return _get_dir_size_recursive(path)

    @staticmethod
    def get_dir_size_iterative(path):
        """迭代获取文件夹大小，单位：Bytes"""
        size = 0
        name_dir = [path]
        # name_dir是一个栈，存放目录名
        while name_dir:
            # 从栈中取出一个目录并获取目录下的文件名。海象运算符“:=”可以先计算表达式再赋值
            try:
                name_list = os.listdir(ret := name_dir.pop())
            except PermissionError:
                continue
            for i in name_list:
                j = f'{ret}/{i}'
                if os.path.isfile(j):
                    try:
                        size += os.path.getsize(j)
                    except PermissionError:
                        pass
                else:
                    name_dir.append(j)  # 如果是目录，压入栈中
        return size

    @staticmethod
    def get_dir_size_os_walk(path):
        """os.walk()获取文件夹大小，单位：Bytes
        os.walk()返回一个三元组(root, dirs, files)，root是当前目录路径，dirs是当前目录下的子目录，files是当前目录下的文件。
        有多少个文件夹（包括当前目录和所有子目录）就有多少个三元组。

        经测试，os.walk()方法最快，其次是迭代方法，递归方法最慢
        """
        size = 0
        for root, dirs, files in os.walk(path):
            for name in files:
                try:
                    size += os.path.getsize(f'{root}/{name}')
                except (OSError, PermissionError):
                    # 捕获OSError和PermissionError异常，并跳过无法访问的文件
                    continue
        return size

    @staticmethod
    def get_size(path_):
        """
        获取文件或目录大小，如果是目录，返回目录下所有文件大小之和。注意，若目录包含子目录，子目录下文件大小不计算在内
        :param path_: 文件或目录路径
        :return: 文件或目录大小，单位：Bytes
        :exception: 如果路径不存在，或者路径既不是文件也不是目录，抛出异常
        """
        if not os.path.exists(path_):
            raise ValueError("The path does not exist: %s" % path_)
        if FileUtil.is_file(path_):
            return os.path.getsize(path_)
        elif FileUtil.is_dir(path_):
            return FileUtil.get_dir_size_os_walk(path_)
        else:
            raise ValueError("The path is not a file or directory: %s" % path_)

    @staticmethod
    def get_one_level_sub_dir_info(directory_path_: str) -> list[{}]:
        """
        获取一级子文件夹信息，包括文件夹路径、名称、大小、创建时间、修改时间、访问时间
        os.scandir()方法返回一个迭代器，迭代器的每个元素是一个DirEntry对象，包含文件或目录的路径、体积、时间等元信息
        :param directory_path_: 目标文件夹路径"""
        # 判断directory_path是否为目录
        if not FileUtil.is_dir(directory_path_):
            raise ValueError("The path is not a directory: %s" % directory_path_)
        iterator = os.scandir(directory_path_)
        dir_info_list = []
        for dirEntity in iterator:
            if dirEntity.is_dir():
                path_ = dirEntity.path
                stat_ = dirEntity.stat()
                dir_info_list.append(
                    {
                        "path": path_,
                        "name": dirEntity.name,
                        "size": FileUtil.get_dir_size_iterative(path_),
                        "create_time": stat_.st_ctime,
                        "update_time": stat_.st_mtime,
                    }
                )
        return dir_info_list
