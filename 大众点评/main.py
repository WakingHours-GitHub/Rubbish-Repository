import re
import time

import requests
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxOptions
# om selenium.webdriver import ChromeOptions


# pip install fontTools


headers = {
    "User-Agent": UserAgent().random,
    "Referer": "https://www.dianping.com"

}
"""
 .tagName{
    font-family: 'PingFangSC-Regular-tagName';
}
@font-face{
    font-family: "PingFangSC-Regular-shopNum";
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/fbb39843.eot");
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/fbb39843.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/fbb39843.woff");
}
 .shopNum{
    font-family: 'PingFangSC-Regular-shopNum';
}
@font-face{
    font-family: "PingFangSC-Regular-reviewTag";
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.eot");
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.woff");
}
"""


def download_woff_file(url: str):
    print(url)
    css_resp = requests.get("http:" + url, headers=headers)
    print(css_resp.text)

    tagName_woff_href = re.search(
        r'@font-face\{font-family: "PingFangSC-Regular-tagName";src:url\(".*?"\);src:url\(".*,url\("(?P<href>.*?)"\);',
        css_resp.text, re.S).group("href")
    shopNum_woff_href = re.search(
        r'@font-face\{font-family: "PingFangSC-Regular-shopNum";src:url\(".*?"\);src:url\(".*,url\("(?P<href>.*?)"\);',
        css_resp.text, re.S).group("href")
    print(tagName_woff_href, shopNum_woff_href)
    with open("./file/tagName_woff.woff", 'wb') as f_write:
        resp = requests.get("http:" + tagName_woff_href, headers=headers)
        f_write.write(resp.content)
    with open("./file/shopNum_woff.woff", 'wb') as f_write:
        resp = requests.get("http:" + shopNum_woff_href, headers=headers)
        f_write.write(resp.content)

    # 转换：
    tagName_woff = TTFont("./file/tagName_woff.woff")
    tagName_woff.saveXML("./file/tagName_woff.xml")

    shopNum_woff = TTFont("./file/shopNum_woff.woff")
    shopNum_woff.saveXML("./file/shopNum_woff.xml")


# def get_woff_file(resp) -> None:
#     '    <link rel="stylesheet" type="text/css" href="//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/9c6bca2c826cc983ecfdf2cba5a76c10.css">'
#     result = re.findall(r'<link rel="stylesheet" type="text/css" href="(.*?)">', resp.text)
#     print(result)

def get_sub_url(url: str) -> None:
    pass

def main2() -> None:
    # 选择 Chrome 浏览器并打开
    # options = Options()
    # options.add_argument("--disable-blink-features")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    option = FirefoxOptions()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument("--disable-blink-features=AutomationControlled")
    main_url = 'http://www.dianping.com/search/keyword/2/0_%E7%B4%A0%E9%A3%9F%E9%A4%90%E5%8E%85'
    firefox = webdriver.Firefox(options=option)

    firefox.get(main_url)

    time.sleep(10)

    firefox.close()
    firefox.quit()


def main() -> None:
    # main_url = "https://www.dianping.com/search/keyword/2/0_%E7%B4%A0%E9%A3%9F%E9%A4%90%E5%8E%85"
    main_url = 'http://www.dianping.com/search/keyword/2/0_%E7%B4%A0%E9%A3%9F%E9%A4%90%E5%8E%85'
    resp = requests.get(main_url, headers=headers)
    print(resp.text)
    # get_woff_file(resp)
    # return
    #
    resp.encoding = "utf-8"
    # 一页的内容：

    e = etree.HTML(resp.text)  # create etree object
    '//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[1]/a'
    store_url_list = e.xpath('//*[@id="shop-all-list"]/ul/li[*]/div[2]/div[1]/a/@href')
    comment_num_lit = e.xpath('string(//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[2]/a[1]/b)')
    css_href = e.xpath('//link/@href')[8]
    download_woff_file(css_href)

    print(css_href)
    print(comment_num_lit)
    return

    for store_url in store_url_list:
        get_sub_url(store_url)
        break
    # print(store_url_list)

    pass

if __name__ == '__main__':
    main()

"""
woff file: saved 'woff' format font type data
@font-face{
    font-family: "PingFangSC-Regular-address";
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.eot");
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.woff");
}
 .address{
    font-family: 'PingFangSC-Regular-address';
}
@font-face{
    font-family: "PingFangSC-Regular-tagName";
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6dec555e.eot");
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6dec555e.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6dec555e.woff");
}
 .tagName{
    font-family: 'PingFangSC-Regular-tagName';
}
@font-face{
    font-family: "PingFangSC-Regular-shopNum";
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/fbb39843.eot");
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/fbb39843.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/fbb39843.woff");
}
 .shopNum{
    font-family: 'PingFangSC-Regular-shopNum';
}
@font-face{
    font-family: "PingFangSC-Regular-reviewTag";
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.eot");
    src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/6cb3e44e.woff");
}
 .reviewTag{
    font-family: 'PingFangSC-Regular-reviewTag';
}



"""
