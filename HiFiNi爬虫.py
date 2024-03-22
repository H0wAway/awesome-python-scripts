import json
import re
import sys
from urllib.parse import quote

import bs4
import requests
from bs4 import BeautifulSoup

# 请求标头一定要和实际一致，例如User-Agent、Referer等都是简单的反爬虫手段
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


def get_request(url, referer):
    headers_copy = headers.copy()
    # headers添加Referer
    headers_copy['Referer'] = referer
    headers_copy['Cookie'] = cookies
    # 发送GET请求
    response = requests.get(url, headers=headers_copy)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    else:
        # 请求失败的原因
        print(response.status_code, response.reason)
        return None

# TODO BUG 有时候不需要点击VIP按钮就能获取到提取码，但是代码中默认点击了VIP按钮，导致提取码错误
# TODO 解决思路：判断第一个链接对应的提取码是否需要点击VIP按钮，如果不需要，就不点击，如果需要，就点击
# 解析get_song_detail返回的html，获取歌曲下载链接和提取码
def parse_song_detail(html: str, referer: str) -> object:
    """
    # 下载链接+提取码对应HTML：
    <p><a href="https://pan.baidu.com/s/1rckm4TWs-HneDA6UrJcsbA" target="_blank">https://pan.baidu.com/s/1rckm4TWs-HneDA6UrJcsbA</a></p>
    <div class="alert alert-success" role="alert">
    <button type="button" class="btn btn-default  btn-block" data-modal-url="my-vip_pan_code.htm?key=bSIZ3fX0ztS37Oj8bCwdFNNCyGJheyWSk5knkg" data-modal-title="提取码" data-modal-size="lg">******    VIP点击免费获取   ******</button></div>
    """
    if html is None:
        return None
    try:
        soup2 = BeautifulSoup(html, 'html.parser')
        # 提取码需要点击一下（此处默认取第一个度盘分享链接和第一个提取码）
        share_link = soup2.find('a', href=lambda value: value and value.startswith("https://pan.baidu.com/s/"))['href']
        code_link = "https://www.hifini.com/" + soup2.find('button', {'data-modal-title': '提取码'})['data-modal-url']
        # 对code_link发送GET请求，
        code = parse_code_page(get_request(code_link, referer))
        # 带提取码的度盘链接：share_link?pwd=code
        return share_link + "?pwd=" + code
    except Exception as e:
        print(e)
        return None


# 解析提取码页面
def parse_code_page(html: str):
    if html is None:
        return None
    # 按顺序提取class值对应style属性为display: inline对应的span标签的内容
    """示例
    <main id="body">
      <div class="container">
        <style>
          .v_if_HgQF8_VF,
          .l_iz_zO_rp {
            display: inline !important;
          }
          .x_yv_Rvjba_Wj1 {
            display: none !important;
          }
        </style>
        <div class="v_pan_code alert alert-info">
          <h4>
            <span class="x_yv_Rvjba_Wj1">j</span>
            <span class="v_if_HgQF8_VF">4</span>
            <span class="l_iz_zO_rp">r</span>
          </h4>
        </div>
      </div>
    </main>
    """
    soup3 = BeautifulSoup(html, 'html.parser')
    # 找到包含提取码的div标签中h4标签
    h4_element = soup3.find('div', class_='v_pan_code').find('h4')
    # 使用正则表达式匹配具有 display: inline 样式的span标签
    span_elements = h4_element.find_all('span')
    extracted_code = ''
    for span in span_elements:
        # span的类型为bs4.element.Tag
        if not isinstance(span, bs4.element.Tag):
            continue
        class_name = span['class'][0]
        style_element = soup3.find('main', {'id': 'body'}).find('style').text
        if is_class_display(class_name, style_element):
            extracted_code += span.text
    return extracted_code


# 判断class_name对应的style属性是否为display: inline
def is_class_display(class_name, style_element):
    index_class = style_element.find(class_name)
    index_display_inline = style_element.find('inline')
    # 有点问题的，可能没有display属性，但浏览器默认为display: inline
    if index_class == -1 or index_display_inline == -1:
        print("style不合一般情况——————class_name: " + class_name + " style: " + style_element)
        return False
    elif index_class > index_display_inline:
        return False
    return True


if __name__ == '__main__':
    # 自行抓取，vip账户海鲜平台可租
    cookies = "bbs_sid=taiv5o6tjhgjnsd89hsoe81ga2; bbs_token=qAKPSiulb0KeTsFTj3Kh7aMOFHuwaHg0L6yGKlyRS5YmSOBH9GVUEZOAIu9evZbo013m0FbJn1_2BFtR7RLB2qbXsNOZtw1MpP; 209d686bd9a11b36b2a10d683dce4525=f02833e84654fe4d206b46baa30736cb; 772f075b5906b913d76fa7aefd95aff7=84c9700058c6eecab84285e513bc855f"
    # 高级搜索，+表示and，-表示not，字母不会区分大小写
    search_keyWord = "周杰伦+flac -[失效]"
    # 进行URL编码,并将%替换为_
    encoded_string = quote(search_keyWord.replace('%', '_'))
    song_list = []
    for i in range(1, 2):
        search_url = "https://www.hifini.com/search-" + encoded_string + "-1-" + str(i) + ".htm"
        search_result = get_request(search_url, "https://www.hifini.com/search.htm")
        # 如果搜不到，也会返回200，但是内容是“暂无结果, 请发帖说明”
        if search_result is None or "暂无结果" in search_result or "\"code\": \"0\"" in search_result:
            print(json.dumps(song_list, indent=4, ensure_ascii=False))
            print("搜索结果为空,退出")
            sys.exit(0)
        print("搜索页网络信息：" + search_url)
        soup = BeautifulSoup(search_result, 'html.parser')
        card_header = soup.find_all('div', class_='card-header')
        # 找到所有包含 data-tid 属性的列表项,特征为 class 属性以 media thread 开头
        thread_items = soup.find_all('li', class_=lambda value: value and value.startswith('media thread'))
        # 遍历每个列表项，提取 data-tid 和链接的值
        for thread_item in thread_items:
            tid = thread_item['data-tid']
            subject_element = thread_item.find('div', class_='subject break-all')
            href = subject_element.find('a')['href']
            href_text = subject_element.find('a').get_text(strip=True)  # 去除空白和 <em> 标签
            if "[失效]" in href_text or "《" not in href_text or "FLAC" not in href_text:
                print("不符要求的标题" + href_text)
                continue
            else:
                matches = re.findall(r'《(.*?)》', href_text)
            thread_info = {'tid': tid, 'title': href_text, 'name': matches[0], 'href': href}
            print("详情页网络信息：" + json.dumps(thread_info, ensure_ascii=False))
            detail_url = "https://www.hifini.com/" + href
            # 设置X-Requested-With: XMLHttpRequest请求头
            headers['X-Requested-With'] = "XMLHttpRequest"
            thread_info['dubox'] = parse_song_detail(get_request(detail_url, search_url), detail_url)
            song_list.append(thread_info)
    print(json.dumps(song_list, indent=4, ensure_ascii=False))
