import random
from paho.mqtt import client as mqtt_client

# mqtt连接
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # 设置回调函数
    client.on_connect = on_connect
    client.connect('broker-cn.emqx.io', 1883)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(("/edge/3311101193/3311101193/rtg", "/edge/3311101194/3311101194/rtg",
                      "/edge/3311079048/3311079048/rtg", "/edge/3311079057/3311079057/rtg",
                      "/edge/3311079053/3311079053/rtg"))
    # 设置回调函数
    client.on_message = on_message


def mqtt_run():
    client = connect_mqtt()
    subscribe(client)
    # 循环监听消息
    client.loop_forever()


if __name__ == '__main__':
    mqtt_run()
    print(1)
