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
