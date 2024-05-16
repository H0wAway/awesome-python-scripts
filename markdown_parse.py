import re
import urllib.parse as url_util

import markdown

import ai_util as ai
from utils import *


def find_image_matches(content_):
    """查找 markdown 文件中的图片链接
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
        print("文件备份到：", FileUtil.file_backup(path))
        with open(path, 'r', encoding='utf-8') as file:
            content_ = file.read()
        matches = find_image_matches(content_)
        for match in matches:
            content_ = content_.replace(match.group(2), url_quoto(match.group(2)))
        if FileUtil.write_file(path, content_, 'w'):
            print("修改后的文件已保存至:", path)
        else:
            print("文件保存失败，请检查路径是否正确。")
    except FileNotFoundError:
        print("文件未找到，请检查路径是否正确。")
    except Exception as e:
        print("发生错误：", e)


def md2html(path_: str):
    """由markdown文件生成html代码并应用github-markdown样式
    :param path_: markdown文件路径
    """
    html = markdown.markdown(open(path_, 'r', encoding='utf-8').read())
    # 注意需要用<article class="markdown-body">标签包住
    html_with_style = f"""<!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" 
         href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    </head>
    <body>
    <article class="markdown-body">
    {html}
    </article>
    </body>
    </html>
"""
    FileUtil.write_file(FileUtil.path_change_extension(path_, 'html'), html_with_style, 'w')


def compress_code_formate(path_: str):
    """
    将markdown文件中的压缩代码块格式化
    :param path_: 文件路径
    :return: None
    """
    print("文件备份到：", FileUtil.file_backup(path_))

    with open(path_, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)  # 回到文件开头
        content_ = file.read()
    i = 0
    while i < len(lines):
        line_ = lines[i].strip()  # 去除首尾空白字符
        if line_.startswith("```") and i + 1 < len(lines) and lines[i + 2].strip().endswith("```"):
            language = line_.replace("```", "")  # 提取语言
            indentation = lines[i].find("`")  # 提取缩进
            code = lines[i + 1]  # 提取单行的压缩的代码，不需要去除首尾空白字符
            print(f"语言：{language}, 缩进：{indentation}，代码：{code}")
            # 使用openai的f2gpt_chat接口格式化代码
            format_code = ai.f2gpt_chat(
                f"将以下{language}代码格式化，只需要结果不要其他无关描述：\n{code}"
            )
            format_code = StrUtil.add_char_to_lines(format_code, indentation)
            print("格式化后的代码：\n", format_code)
            content_ = content_.replace(code, format_code)
            i += 2
        else:
            i += 1
    if FileUtil.write_file(path_, content_, 'w'):
        print("修改后的文件已保存至:", path_)


if __name__ == "__main__":
    # r""表示引号内为原始字符串（raw string）, 故不需要转义
    file_path = r"E:\工作记录.md"
    # md_url_encode(file_path)
    md_path = r"C:\参数校验.md"
    compress_code_formate(md_path)
    # md2html(md_path)
