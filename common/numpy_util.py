import numpy as np


# 根据输入参数，生成矩阵
def generate_matrix(rows: int, cols: int, start: int = 0, step: int = 1) -> np.ndarray:
    """
    根据输入参数，生成矩阵
    :param rows: 行数
    :param cols: 列数
    :param start: 起始值
    :param step: 步长
    :return: np.ndarray
    """
    return np.arange(start, rows * cols * step, step).reshape(rows, cols)


# 计算一维ndarray的均值、最大值、最小值、中位数、方差、标准差
def calculate_1d_array(arr: np.ndarray) -> dict:
    """
    计算一维ndarray的均值、最大值、最小值、中位数、方差、标准差、数据量、众数以及众数出现的次数
    :param arr: 一维ndarray
    :return: dict
    """
    return {
        'mean': np.mean(arr),
        'max': np.max(arr),
        'min': np.min(arr),
        'median': np.median(arr),
        'var': np.var(arr),
        'std': np.std(arr),
        'size': arr.size,
        'mode': np.argmax(np.bincount(arr)),
        'mode_count': np.bincount(arr).max()
    }
