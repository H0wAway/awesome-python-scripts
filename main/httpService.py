import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.DEBUG)


@app.route('/api/secp-iot-mqtt-auth/v2/auth/check', methods=['POST'])
def check_auth():
    # 获取请求的数据
    data = request.get_data()
    # 打印请求数据
    print(f"Received data: {data}")
    # 返回固定的响应体
    response_body = {"result": "allow", "is_superuser": False}
    return jsonify(response_body)


@app.route('/api/ds/emqx/event', methods=['POST'])
def receive_event():
    # 获取请求的数据
    data = request.get_data()
    print(f"Received data: {data}")
    # 返回固定的响应体
    response_body = {"result": "ok"}
    return jsonify(response_body)


if __name__ == '__main__':
    # 启动Flask应用，监听在9009端口
    app.run(host='0.0.0.0', port=9009)
