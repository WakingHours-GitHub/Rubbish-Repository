"""
http://172.17.100.10:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=201923020986&user_password=FWJ%4015246337585&wlan_user_ip=10.100.214.141&wlan_user_ipv6=&wlan_user_mac=90ccdfd07a82&wlan_ac_ip=&wlan_ac_name=me60&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=5154&lang=zh
"""
import time
import requests
from fake_useragent import UserAgent
import socket # 使用自带的socket库
import uuid
import json


def get_mac():
    r""" 针对单网卡 """
    addr = hex(uuid.getnode())[2:].upper()

    return '-'.join(addr[i:i + 2] for i in range(0, len(addr), 2))
# from urllib import parse
# 函数 gethostname() 返回当前正在执行 Python 的系统主机名
local_ip = socket.gethostbyname(socket.gethostname()) #
local_mac = get_mac().replace("-","")
print(local_ip)
print(local_mac)
# 实验室登录的url
# url = "http://172.17.100.10:801/eportal/portal/login"
"""http://172.17.100.10:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=201923020986&user_password=FWJ%4015246337585&wlan_user_ip=10.200.185.55&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=7472&lang=zh"""
url = "http://172.17.100.10:801/eportal/portal/login?"




"""
regex: 
(\w.*?): (.*)
"$1" :"$2" ,
"""
params = {
    "callback": "dr1003",
    "login_method": "1",
    "user_account": "201923020986",
    "user_password": "FWJ@15246337585",
    "wlan_user_ip": local_ip.__str__(), # local ip
    "wlan_user_ipv6": "", #
    "wlan_user_mac": local_mac,
    "wlan_ac_ip": "",
    "wlan_ac_name": "me60",
    "jsVersion": "4.1",
    "terminal_type": "1",
    "lang": "zh-cn",
    # "v": "5154", # 该参数会变动
    # "v": "7472",
    # "lang": "zh",
}


headers = {
    "User-Agent": UserAgent().chrome
}

while True:
    try:
        resp_test = requests.get(url, headers=headers, params=params, timeout=5)
        print("status_code", resp_test.status_code)
        if resp_test.status_code == 200:
            while True:
                resp = requests.get(url, headers=headers, params=params, timeout=5)
                dict_str = resp.text[resp.text.find("{"): resp.text.rfind("}")+1]

                resp_dict = json.loads(dict_str)

                print(resp_dict)
                if resp_dict['ret_code'] != 2:
                    print("[ERROR]")
                time.sleep(1)


    except Exception as e:
        print(e)
        print("[ERROR]: please connect network of school.")
        print("Please connect network of school manually, programming loop until you connect network")


    finally:
        pass
        # resp.close()




exit(0)
