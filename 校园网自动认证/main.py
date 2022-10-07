"""
http://172.17.100.10:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=201923020986&user_password=FWJ%4015246337585&wlan_user_ip=10.100.214.141&wlan_user_ipv6=&wlan_user_mac=90ccdfd07a82&wlan_ac_ip=&wlan_ac_name=me60&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=5154&lang=zh
"""
import requests
from fake_useragent import UserAgent
import socket # 使用自带的socket库
# from urllib import parse
# 函数 gethostname() 返回当前正在执行 Python 的系统主机名
local_ip = socket.gethostbyname(socket.gethostname()) #

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
    "wlan_user_mac": "90ccdfd07a82",
    "wlan_ac_ip": "",
    "wlan_ac_name": "me60",
    "jsVersion": "4.1",
    "terminal_type": "1",
    "lang": "zh-cn",
    "v": "5154", # 该参数会变动
    # "v": "7472",
    "lang": "zh",
}


headers = {
    "User-Agent": UserAgent().chrome
}

resp = requests.get(url, headers=headers, params=params)

print(resp.text)
