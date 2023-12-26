from confluent_kafka import Producer
import ast
import json

# Kafka 服务器地址和端口
# bootstrap_servers = '192.168.221.233:9092'
bootstrap_servers = '192.168.221.114:9092'

# 主题名称
topic = 'secp-blade-runner'

# 配置生产者
conf = {'bootstrap.servers': bootstrap_servers}

# 创建生产者实例
producer = Producer(conf)


def dahua_warn():
    # 发送消息
    json_msg = '[{\"alarmType\":2,\"msgType\":\"videoMotion\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"},{\"alarmType\":2,\"msgType\":\"videoBlind\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"},{\"alarmType\":2,\"msgType\":\"aiPerArea\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"},{\"alarmType\":2,\"msgType\":\"fireAlarm\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"},{\"alarmType\":2,\"msgType\":\"smokingDetect\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"},{\"alarmType\":2,\"msgType\":\"heatImagingTemper\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"},{\"alarmType\":2,\"msgType\":\"aiPerLine\",\"picUrlArray\":[\"123\",\"https://yr-bA%3D\"],\"alarmId\":\"1890132516586096\",\"messageId\":\"62c96a2b-c40b-48c0-9548-c8f82f92a48c\",\"channelName\":\"test8B054B6PAZ86DF0-2\",\"time\":1703463698000,\"storeId\":261254379725144060,\"deviceId\":\"test8B054B6PAZ86DF0\",\"deviceName\":\"test8B054B6PAZ86DF0\",\"channelId\":\"1\"}]'
    parsed_list = ast.literal_eval(json_msg)
    if isinstance(parsed_list, list):
        print('成功解析为列表')
        # print(parsed_list)
    else:
        print("提供的字符串不是有效的列表表示。")
    for message in parsed_list:
        msg = json.dumps(message)
        producer.produce(topic, key='dahua-warn', value=msg)
        print('发送消息：', msg)


dahua_warn()


# 刷新并关闭生产者
producer.flush()
