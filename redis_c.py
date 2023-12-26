import redis

# 连接到Redis服务器
redis_client = redis.StrictRedis(host='192.168.1.169', port=6389, db=3, password='goodwe', decode_responses=True)

hash_name = "secp:dyson-sphere:device:test123213"
key = "ICCID"
value = "testtest"

# 将数据存入redis
result = redis_client.hset(hash_name, key, value)

# 检查存储结果并打印消息
if result == 1:
    print(f"数据存入成功：{hash_name}[{key}] = {value}")
else:
    print(f"数据存入失败：可能是hash已经存在或其他原因。")
