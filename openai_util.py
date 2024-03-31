from enum import Enum

from environs import Env
from openai import OpenAI

env = Env()
env.read_env()


# 创建枚举类，区分不同的OpenAI API
class OpenAIEnum(Enum):
    f2gpt = "OPEN_AI_f2gpt"
    chatGPT = "OPEN_AI_chatGPT"


def get_openai_client(api_enum: OpenAIEnum) -> OpenAI:
    """获取OpenAI的客户端
    从.env中获取OpenAI的配置信息，创建OpenAI客户端
    Env Example:
        OPEN_AI_f2gpt={"url":"https://api.openai.com","key":"sk-xxx"}
    """
    j1 = env.json(api_enum.value)
    client = OpenAI(organization=api_enum.name)
    client.base_url = j1.get("url")
    client.api_key = j1.get("key")
    return client


def stream_output(client_):
    """流式输出来自chatGPT的结果"""
    stream = client_.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "以中文回复。一句话说明Postgresql索引的底层逻辑"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


def none_stream_output(client_: OpenAI, content_):
    """None stream output from the chatGPT."""
    response = client_.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content_}],
    )
    return response.choices[0].message.content


f2_client = get_openai_client(OpenAIEnum.f2gpt)


def f2gpt_chat(content_):
    # f2_client 类型检查
    if isinstance(f2_client, OpenAI):
        return none_stream_output(f2_client, content_)
    else:
        return "f2_client is not OpenAI type"
