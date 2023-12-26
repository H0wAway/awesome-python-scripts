import os
import re
import requests


def download_images_and_update_links(markdown_file):
    # 创建assets文件夹
    if not os.path.exists("assets"):
        os.makedirs("assets")

    # 读取Markdown文件内容
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式匹配图片信息
    pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    matches = re.findall(pattern, content)

    for match in matches:
        image_title, image_url = match

        # 下载图片
        response = requests.get(image_url, allow_redirects=True)
        if response.status_code == 200:
            # 获取文件扩展名
            extension = os.path.splitext(image_url)[1]
            # 构造保存的文件名
            image_filename = f"{image_title}{extension}"
            # 保存图片到assets文件夹
            image_path = os.path.join("assets", image_filename)
            with open(image_path, 'wb') as img_file:
                img_file.write(response.content)

            # 更新Markdown文件中的链接为相对路径
            relative_path = os.path.join("assets", image_filename)
            content = content.replace(image_url, relative_path)

    # 将更新后的内容写回Markdown文件
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    # 替换为你的Markdown文件路径
    markdown_file_path = "your_markdown_file.md"
    download_images_and_update_links(markdown_file_path)
