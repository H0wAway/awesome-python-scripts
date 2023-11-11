# os库用于文件操作
import os

# 移除文件末尾的".下载"后缀
def main():
    directory = r"E:\Desktop\WE-PLATFORM_files"
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否以".下载"结尾
        if filename.endswith(".下载"):
            # 构造新的文件名（移除".下载"）
            new_filename = filename[:-len(".下载")]
            # 构造完整的文件路径
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed "{filename}" to "{new_filename}"')


# 筛选出简历中的名字 格式：【物联网工程师_苏州】你的名字 24年应届生
def resume_name():
    resume = r"E:\Desktop\物联网11.9"
    list1 = []
    for filename in os.listdir(resume):
        start_index = filename.index("】")
        end_index = filename.index("24年应届生") - 1
        name = filename[start_index + 1:end_index].strip()
        list1.append(name)
    print(list1)


if __name__ == "__main__":
    # main()
    # resume_name()
    print("----------------------------------1")
