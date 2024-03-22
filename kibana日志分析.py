import re


# 打开输入文件和输出文件

global input_file, output_file, lines, line


def method_name2():
    global input_file, output_file, lines, line
    with open('E:\\Downloads\\20min.txt', 'r', encoding='utf-8') as input_file, open(
        'E:\\Downloads\\1.txt', 'w'
    ) as output_file:
        lines = input_file.readlines()
        # 初始化一个标志变量，用于指示是否应该将下一行数据写入输出文件
        write_next_line = False
        my_list = [0]
        # 遍历每一行数据
        for line in lines:
            # 如果当前行包含403，则设置标志变量为True
            if '[403]' in line:
                write_next_line = True
            # 如果标志变量为True，将当前行写入输出文件，并将标志变量重新设置为False
            elif write_next_line:
                match = re.search(r'clientId=(\d+),\s+username=(\d+)', line)
                if match:
                    # 提取到clientId和username的值
                    client_id = match.group(1)
                    username = match.group(2)
                    if (client_id == username) & ('clientId=3' in line):
                        if not my_list.__contains__(int(client_id)):
                            my_list.append(int(client_id))
                            print('不重复')

                write_next_line = False
        my_list.sort()
        print(my_list)


# 删除空白行
def method_name():
    global input_file, output_file, lines, line
    with open('E:\\Downloads\\10min.txt', 'r', encoding='utf-8') as input_file, open(
        'E:\\Downloads\\20min.txt', 'w', encoding='utf-8'
    ) as output_file:
        lines = input_file.readlines()

        # 遍历每一行数据
        for line in lines:
            # 如果当前行不是空白行，则将其写入输出文件
            if line.strip():
                output_file.write(line)


if __name__ == '__main__':
    list1 = [
        320203117,
        3202012982,
        3202030796,
        3202031056,
        3202031072,
        3202031113,
        3202031161,
        3202031286,
        3205069730,
        3205069776,
        3205069790,
        3205069987,
        3207150713,
        3207150732,
        3207150760,
        3207150767,
        3207150815,
        3207150867,
        3207150888,
        3207150943,
        3207150944,
        3208000242,
        3208000261,
        3211014330,
        3212155495,
        3305080930,
        3305080959,
        3305080980,
        3305107286,
        3305107306,
        3305107319,
        3305107401,
        3305107464,
        3305107578,
        3305107668,
        3305107679,
        3305107700,
        3309042011,
        3207150949,
        3305081034,
    ]
    method_name()
    method_name2()
