from utils import FileUtil

"""
备份文件夹清理，保留最新的文件夹，删除没有变化的文件夹
"""
path_ = r"/opt/pgsql_table1_backup"
dir_info_list = FileUtil.get_one_level_sub_dir_info(path_)

# 按照create_time升序排序
dir_info_list = sorted(dir_info_list, key=lambda x: x.get('create_time'), reverse=False)
# 若相邻多个文件夹的size相同，则保留第一个，删除后面的
length = len(dir_info_list)
list_to_remove = []
for i in range(length - 1):
    if dir_info_list[i].get('size') == dir_info_list[i + 1].get('size'):
        print(f"重复文件夹：{dir_info_list[i].get('path')}")
        list_to_remove.append(dir_info_list[i + 1])

for item in list_to_remove:
    FileUtil.delete(item)
