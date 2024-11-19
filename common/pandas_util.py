import pandas as pd
from pandas import DataFrame


def print_df_info(df: DataFrame) -> None:
    """打印 DataFrame 的基本信息"""
    print("Pandas 版本：", pd.__version__)
    print("前 5 行数据：\n", df.head())
    print("后 5 行数据：\n", df.tail())
    print("数据信息：")
    df.info()
    print("数据描述统计：\n", df.describe())
    print("列名：\n", df.columns)
    print("索引：\n", df.index)
    print("DataFrame 类型：", type(df))
    # 打印列名及其对应的数据类型
    print("列名及其对应的数据类型：")
    for col, dtype in df.dtypes.items():
        print(f"{col}: {dtype}")


def batch_drop(df: DataFrame, columns: list[int], rows: list[int]) -> None:
    """批量删除行和列
    :param columns: 要删除的列索引列表
    :param rows: 要删除的行索引列表
    :param df: DataFrame 对象
    """
    # axis=0 表示删除行，axis=1 表示删除列
    df.drop(df.columns[columns], axis=1, inplace=True)
    # inplace 表示就地, 如果为 False，则返回副本。否则，就地操作并返回 None
    df.drop(index=rows, axis=0, inplace=True)


def column_rename(df: DataFrame, mapping_dict: dict[int, str]) -> None:
    """重命名列名
    :param df: DataFrame 对象
    :param mapping_dict: 列索引和新列名的映射字典
    """
    df.rename(columns=mapping_dict, inplace=True)
