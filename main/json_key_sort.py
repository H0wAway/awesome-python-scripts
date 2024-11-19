import json
import re


def custom_sort_key(key):
    # 使用正则表达式提取字段中的数字部分，并返回一个元组 (前缀, 数字)
    match = re.match(r"(\D+)(\d+)", key)
    if match:
        prefix = match.group(1)  # 提取非数字部分
        number = int(match.group(2))  # 提取数字部分并转为整数
        return prefix, number
    return key, 0  # 处理没有数字的键


def sort_json(data, ascending=True):
    # 对字典的键按照自定义规则排序
    sorted_data = dict(sorted(data.items(), key=lambda item: custom_sort_key(item[0]), reverse=not ascending))
    return sorted_data


# 示例 JSON 数据
json_data = """{"tInPackNeg":24.6,"tIn15":3.275,"tIn14":3.275,"tIn17":3.275,"tIn16":3.275,"tIn11":3.275,
"tIn10":3.274,"tIn13":3.274,"tIn12":3.276,"sendTp":1729563124000,"tIn19":3.276,"tIn18":3.275,"tInPackPos":24,
"tIn20":3.276,"tIn26":3.274,"tIn25":3.276,"tIn28":3.274,"tIn27":3.275,"tIn22":3.273,"tIn21":3.274,"tIn24":3.274,
"tIn23":3.275,"tIn29":3.275,"tIn31":3.275,"tIn30":3.274,"u11":3.275,"u10":3.274,"u13":3.274,"u12":3.276,"u15":3.275,
"tIn37":3.275,"u14":3.275,"tIn36":3.275,"u17":3.275,"tIn39":3.274,"sn":"40041CI022480002","u16":3.275,"tIn38":3.275,
"u1":3.275,"u19":3.276,"tIn33":3.275,"u2":3.275,"u18":3.275,"tIn32":3.275,"u3":3.275,"tIn35":3.275,"u4":3.274,
"tIn34":3.275,"u5":3.275,"u6":3.275,"product":"gw-ci-bms-rack-pack-1","u7":3.275,"u8":3.275,"u9":3.274,"tIn40":3.274,
"u20":3.276,"tIn42":3.276,"tIn41":3.275,"u22":3.273,"u21":3.274,"u24":3.274,"u23":3.275,"u26":3.274,"tIn48":3.274,
"u25":3.276,"tIn47":3.276,"u28":3.274,"u27":3.275,"tIn49":3.276,"tp":1729563124000,"tIn44":3.276,"u29":3.275,
"tIn43":3.274,"tIn46":3.275,"tIn45":3.275,"tid":279873364318673300,"tIn51":3.275,"tIn50":3.274,"u31":3.275,
"u30":3.274,"tIn52":3.275,"u33":3.275,"tIn9":3.274,"u32":3.275,"u35":3.275,"u34":3.275,"u37":3.275,"u36":3.275,
"u39":3.274,"u38":3.275,"tIn6":3.275,"tIn5":3.275,"tIn8":3.275,"tIn7":3.275,"tIn2":3.275,"tIn1":3.275,"tIn4":3.274,
"tIn3":3.275,"u40":3.274,"u42":3.276,"u41":3.275,"u44":3.276,"u43":3.274,"u46":3.275,"u45":3.275,"u48":3.274,
"u47":3.276,"u49":3.276,"u51":3.275,"u50":3.274,"u52":3.275,"gate":"23000EZL21B57891"}"""
# 选择升序排列
sorted_json_asc = sort_json(json.loads(json_data), ascending=True)
print("升序排序结果:\n", json.dumps(sorted_json_asc))

# 选择降序排列
# sorted_json_desc = sort_json(json_data, ascending=False)
# print("\n降序排序结果:")
# print(json.dumps(sorted_json_desc, indent=4))
