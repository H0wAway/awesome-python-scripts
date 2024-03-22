import re
import urllib.parse as url_util

import file_utils


def find_image_matches(content_):
    """
    查找 markdown 文件中的图片链接
    !\[(.*?)]\((.*?)\)中，[]和()里面的的()表示分组，方便后面替换. *?表示非贪婪匹配
    :param content_: 匹配的图片链接格式为 ![图片描述](图片链接)，并且图片链接中不包含括号(md规范亦如此)
    :return: 迭代器，每个元素为一个匹配对象x。x.group(0)为整个匹配的字符串，x.group(1)为图片描述，x.group(2)为图片链接
    """
    return re.finditer(r'!\[(.*?)]\((.*?)\)', content_)


def url_quoto(url_: str) -> str:
    """
    对 URL 先进行解码，再进行转义（防止出现已转义的 URL被再次转义），保留 ':' 和 '/'
    :parameter url_: 待转义的 URL 字符串
    :return str: 转义后的 URL 字符串
    """
    # 将 URL 字符串进行解码并替换 '\\' 为 '/'
    decoded_url = url_util.unquote(url_).replace('\\\\', '/')
    # 使用 quote() 方法对 URL 进行转义，保留 ':' 和 '/'
    return url_util.quote(decoded_url, ':/')


def md_url_encode(path) -> None:
    """
    将markdown文件备份，再将其中的图片链接进行URL编码后进行替换
    """
    try:
        print("文件备份到：", file_utils.file_backup(path))
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        matches = find_image_matches(content)
        for match in matches:
            content = content.replace(match.group(2), url_quoto(match.group(2)))
        if file_utils.write_file(path, content, 'w'):
            print("修改后的文件已保存至:", path)
        else:
            print("文件保存失败，请检查路径是否正确。")
    except FileNotFoundError:
        print("文件未找到，请检查路径是否正确。")
    except Exception as e:
        print("发生错误：", e)


if __name__ == "__main__":
    # r""表示引号内为原始字符串（raw string）, 故不需要转义
    file_path = r"E:\goodwe\dw\iot\secp-iot-doc\40-49 项目\46 供应链\禾金泰4.0规约对接工作记录.md"
    md_url_encode(file_path)
