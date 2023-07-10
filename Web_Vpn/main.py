import requests
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver

username = "201923020986"
passward = "FWJ@15246337585"

update_url = "https://webvpn.hrbcu.edu.cn/vpn_key/update"
sign_in_url = "https://webvpn.hrbcu.edu.cn/users/sign_in"
web_vpn_url = "https://webvpn.hrbcu.edu.cn/"


def main() -> None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
        "Referer": "https://webvpn.hrbcu.edu.cn/users/sign_in",
        "Host": "webvpn.hrbcu.edu.cn",
        # "Cookie": "SERVERID=Server1; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAxOTIzMDIwOTg2IiwiZ3JvdXBzIjpbMzAsMjldLCJpYXQiOjE2NzUzNDY2OTgsImV4cCI6MTY3NTQzMzA5OH0.OxLW9dFL-PXtOWuTK46tDKqjS19C3Ss8LWbNj7M9cTA; webvpn_username=201923020986%7C1675346698%7Ccd4cde9f011eda691586adf49f015c3fa837a32a; _webvpn_redirect=1; _astraeus_session=UXgxa3ZDbW4yR3orcVdoRzBLWlE0U1hYd2Uzbm5ZUElrdHA4blBHTXUxaXltNDhlelJjbDBuUUVkOEdSUGpCa2JRN0k3Z1lvR040ZGlqekpuVVNJUC84MmhIUENpc2JtQUVFa2NGTHlJYzZ2RXd2aXJ4WjhsN2txODRrRnNLWld3dFRMb0NyZCtJWGR4U21wT0VENHd1eTF3V0cvcEYwU3VxZlVZUjRYUUlhOXZsNjV4MU9sT296aEV5TTJwQVRUL3BQbU10M1p2clYvNjNjbW1kVHlHZ0xBbWdOczJNWEUvWGJ6UUozRThWR20ySXFtdmFicGRWQTl4akR3TGVDYkM3ZFF3ZE5DMlFjVzdoRUxQNk1YQUdzZTNYOVFsQ0h3d3ZxcHV0eTZjKzFROGNwclM4aEs3blEvcXJNZnJraDJ3d09aVDdzTWFnekhPVHpUV2xFbWlSMmF0K0tQMUZPL2Z1TlVSYmtGTGNwaEVmR1RQeXBQK2g2b0xTbVdXZHlOc3E4WS9RL0t3N2thVUVoYTVQeDFEdz09LS1EK1pzMGhDUGw0VTNzME80b0RtTHBBPT0%3D--aa92511f3098acb260ad34388550e4392adbdacf"
        # "Cookie" : "SERVERID=Server1; _webvpn_key=; webvpn_username=; _astraeus_session=NVJLMEYxTHMzaUl3ZnEzRitKVVEra1F3UjZLdkROMHpMM25JSTlScGF1aXhYZzBCYWY3RzcwblU4ZThTZHVjR3N6NkJPVi9Nd1MrSWFmd3dTZFF3UFhlSXplNzZySjZ2a2tmSXRjbjQ1OFUrQ2FPOGxEaytXTUhMZTV2OE45RHJBQWhsb1JpaytRRmVYVEhya3NyN2krVmg2R3o5WXV1aDkzblVKRnluVGwvOCswZXg0djdsL0V4YkEvSUphQytMbmdXRWhZam03cEx1a0tqVS8rWHJ3cVlPaEZhWE9ZdVdYNytpMDU3b21PejRIV2J4SHhibnhLZ0V0dnBZeWRVUTIvOXNVMWFlUlJwV1YxNkJIbjJLSys4anlpK01LWWEzT0pKQURPNUVIeGxTd3V6bkJiWVVlcS90VVExL3RTRnVEeDVmRWYzSy9VcjNodWwycndxS1lWMitQSXRqeUp3UkYvak5weWhsaUhkZHowUEMrVGlOUUxMc2JjY1lOc2xjYW9Hdm1OKzlJMlhIQWNJRkNWUHMra0ZnUmRqbUlQcnBTQTBNTDRaT1A4TWUrbVk3WHpHODJrU0VuOTZTSXZNRS0tMm9iYzJFc2kxc3JSNG1jSllsQkxCdz09--735dd03a57ab4d9bd83cc319870f39585d5004dd"
        # "Cookie": "SERVERID=Server1; _webvpn_key=eyJhbGciOiJIUzI1NiJ9; webvpn_username=201923020986; _astraeus_session=THFCUlpyVGpabks5Y3ZnVHQ1VlNrbVd4OG8raUNiUm1DSzMySVhZbjUwQS93V3lXMXMvZGRRWDF6YlN0ZHdmTU80UFJNYjFXYVYvUldKN3E3bGFCcFZDelIzUmJTd3NxcFN3Tk10NmFNU011a1VwaVV2SWdPc2RQTUtoLzhwaldkK3lUelNXVm9YQTNLamhrUkdCRlBPT2hlaFFYMkRZNUR4ZHhNUkZJeDQxTEJoc0dIdVg3YTF0QUtNeE52QkVqY2lPNzBONGxGWjlva1FzL2xWNkRRK1ZWSTc5NytPcXQyUjlsZkpXT2plRTFtYzJsL2svelVZazZVRms5SjVsM294YXlXbGZaUXp5eDVxK3oyWnR4aktZT1kxZUF5REc4WVFZdjdMRm83ajNRY1BzemlNOGJNZTNBakhma2pEemR2ZkRhZS9PUGNaWWNRQUlTNEozWnV5RC9tQkRPMUdwbzlVb2RnZEFZeExXY1RpRU5SQitSYXFaRVVBYmdKMTNHbmZkVVZCY0JxRGdOYjM5OE1DTmZPbFordFlOb0NZaU80dWN5cW9ubDkrZ0Z2NTM3WHZJWS81T2h4RDJibjJKWS0tZVR0R1R2VDFHWlVhQUxSTy9ITHp6QT09--8a5e9f78d2aafd0a7b7f8945594eac276b6a79b1",

        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",

        # 一堆不知道是啥的参数:
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": "Windows",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "same-origin",
        # "Sec-Fetch-User": "?1",
        # "Upgrade-Insecure-Requests": "1",
    }
    """
    
    登录页面之前：访问就带有的cookie.
    Cookie: SERVERID=Server1; _webvpn_key=; webvpn_username=; _astraeus_session=THFCUlpyVGpabks5Y3ZnVHQ1VlNrbVd4OG8raUNiUm1DSzMySVhZbjUwQS93V3lXMXMvZGRRWDF6YlN0ZHdmTU80UFJNYjFXYVYvUldKN3E3bGFCcFZDelIzUmJTd3NxcFN3Tk10NmFNU011a1VwaVV2SWdPc2RQTUtoLzhwaldkK3lUelNXVm9YQTNLamhrUkdCRlBPT2hlaFFYMkRZNUR4ZHhNUkZJeDQxTEJoc0dIdVg3YTF0QUtNeE52QkVqY2lPNzBONGxGWjlva1FzL2xWNkRRK1ZWSTc5NytPcXQyUjlsZkpXT2plRTFtYzJsL2svelVZazZVRms5SjVsM294YXlXbGZaUXp5eDVxK3oyWnR4aktZT1kxZUF5REc4WVFZdjdMRm83ajNRY1BzemlNOGJNZTNBakhma2pEemR2ZkRhZS9PUGNaWWNRQUlTNEozWnV5RC9tQkRPMUdwbzlVb2RnZEFZeExXY1RpRU5SQitSYXFaRVVBYmdKMTNHbmZkVVZCY0JxRGdOYjM5OE1DTmZPbFordFlOb0NZaU80dWN5cW9ubDkrZ0Z2NTM3WHZJWS81T2h4RDJibjJKWS0tZVR0R1R2VDFHWlVhQUxSTy9ITHp6QT09--8a5e9f78d2aafd0a7b7f8945594eac276b6a79b1
    
    # update后, 重定向得到的cookie
    Cookie: SERVERID=Server1; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAxOTIzMDIwOTg2IiwiZ3JvdXBzIjpbMzAsMjldLCJpY@XQiOjE2NzUzNDU4MDcsImV4cCI6MTY3NTQzMjIwN30.ztWZZI3WPd_LVaaYxvUpFo8_xyW2Kj4JZLVB0a4VrIk; webvpn_username=201923020986%7C1675345807%7C1aa2e52f633f713a8e739c412873696c64cc10e5; _webvpn_redirect=1; _astraeus_session=MytwY0d3VWxmbkM4VU5Pc2lHWjBQUHFsTjdlem5RWTlybSt3MkVwRk1FbmNzaUExRm5Zb0F6eUFzVVRDNng3NjVVZjNQVHVwQXVkRlN6UVVQalJkenVIcklJdzRiaGV0YlRTWG02a21zVG90SU1mSlMyem9LdGtHRkU2VmZ4UUgzUGNrZ3h4OEhla0htZVYvc2U4cGpjRnhTYThiNTJsc3dJYUNiWXVVNVRzcGNwS1N0RUhKUkQzUU1rZG9WUWo1WXdBQ3FLcW8wcnAvRldYUjZkdGxVVHpPcjZROHJ5UGRrWVlGRDF0THZLQjliSDBRM1htQkZFY2Jjak9UQmFmNUVWd2NMQmhFcGYyY3hNaWdpdDdDK3JNUTc4UlVkZ3pMSHhVRFlnTkpFcHlSMTI2RVEzT1FERzU3dk5JZlNDdVBFYlNtNEJtVUJJamZqWmpzbHFMbDZKS0YrUkhSTHVsT0dQYldnaHBIOW5ocVNEWEk0VEdKd1J3MmNYWkdWbVo5STUwckhaRDZJRjNydjJTQyt2NTU0UT09LS1iUFdqUTk0cVlEa2ovN29QNmE3MkxnPT0%3D--da48390e32931bcd64bcbe40fc603c9d3c9bfb9c
radius_test_password
        _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAxOTIzMDIwOTg2IiwiZ3JvdXBzIjpbMzAsMjldLCJpYXQiOjE2NzUzNDU4MDcsImV4cCI6MTY3NTQzMjIwN30.ztWZZI3WPd_LVaaYxvUpFo8_xyW2Kj4JZLVB0a4VrIk;
         webvpn_username=201923020986%7C1675345807%7C1aa2e52f633f713a8e739c412873696c64cc10e5; 
         
        _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAxOTIzMDIwOTg2IiwiZ3JvdXBzIjpbMzAsMjldLCJpYXQiOjE2NzUzNDY2OTgsImV4cCI6MTY3NTQzMzA5OH0.OxLW9dFL-PXtOWuTK46tDKqjS19C3Ss8LWbNj7M9cTA; 
        webvpn_username=201923020986%7C1675346698%7Ccd4cde9f011eda691586adf49f015c3fa837a32a;
        
        _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAxOTIzMDIwOTg2IiwiZ3JvdXBzIjpbMzAsMjldLCJpYXQiOjE2NzUzNDY2OTgsImV4cCI6MTY3NTQzMzA5OH0.OxLW9dFL-PXtOWuTK46tDKqjS19C3Ss8LWbNj7M9cTA; 
        webvpn_username=201923020986%7C1675346698%7Ccd4cde9f011eda691586adf49f015c3fa837a32a;
        
        
        
        搞明白了: 访问update_url这个域名, 然后判断是否在数据库中, 然后更新状态, 然后重定向到不同的网页(是登录, 还是进入页面)
         
    """

    # update_resp = requests.get(update_url, headers=headers)
    session = requests.Session()
    update_resp = session.get(update_url, headers=headers, allow_redirects=False) # , allow_redirects=False
    # print(update_resp)
    print(update_resp.url)

    if update_resp.url in ("https://webvpn.hrbcu.edu.cn/vpn_key/update", "https://webvpn.hrbcu.edu.cn/users/sign_in"):  # 没有登录
        # headers["Cookie"] = "SERVERID=Server1; _webvpn_key=; webvpn_username=; _astraeus_session=NVJLMEYxTHMzaUl3ZnEzRitKVVEra1F3UjZLdkROMHpMM25JSTlScGF1aXhYZzBCYWY3RzcwblU4ZThTZHVjR3N6NkJPVi9Nd1MrSWFmd3dTZFF3UFhlSXplNzZySjZ2a2tmSXRjbjQ1OFUrQ2FPOGxEaytXTUhMZTV2OE45RHJBQWhsb1JpaytRRmVYVEhya3NyN2krVmg2R3o5WXV1aDkzblVKRnluVGwvOCswZXg0djdsL0V4YkEvSUphQytMbmdXRWhZam03cEx1a0tqVS8rWHJ3cVlPaEZhWE9ZdVdYNytpMDU3b21PejRIV2J4SHhibnhLZ0V0dnBZeWRVUTIvOXNVMWFlUlJwV1YxNkJIbjJLSys4anlpK01LWWEzT0pKQURPNUVIeGxTd3V6bkJiWVVlcS90VVExL3RTRnVEeDVmRWYzSy9VcjNodWwycndxS1lWMitQSXRqeUp3UkYvak5weWhsaUhkZHowUEMrVGlOUUxMc2JjY1lOc2xjYW9Hdm1OKzlJMlhIQWNJRkNWUHMra0ZnUmRqbUlQcnBTQTBNTDRaT1A4TWUrbVk3WHpHODJrU0VuOTZTSXZNRS0tMm9iYzJFc2kxc3JSNG1jSllsQkxCdz09--735dd03a57ab4d9bd83cc319870f39585d5004dd"
        # headers["Cache-Control"] = "no-cache"
        params = {
            # "utf8": "✓",
            # "authenticity_token": "4NyTdLLQnctPJUvgnSH9aXEaWDP6t2dBinfc67/xpPwhzx7HshS52iBRgOtWh9ZavmtFJHMVt7nYZvLSQREDLw==",
            # "user[login]": "201923020986",
            # "user[password]": "FWJ@15246337585",
            # "user[dymatice_code]": "unknown",
            # "user[otp_with_capcha]": "false",
            # "commit": "登录 Login",

            "utf8": "%E2%9C%93",
            # "authenticity_token": "4NyTdLLQnctPJUvgnSH9aXEaWDP6t2dBinfc67%2FxpPwhzx7HshS52iBRgOtWh9ZavmtFJHMVt7nYZvLSQREDLw%3D%3D",
            # "user%5Blogin%5D": "201923020986",
            # "user%5Bpassword%5D": "FWJ%4015246337585",
            # "user%5Bdymatice_code%5D": "unknown",
            # "user%5Botp_with_capcha%5D": "false",
            # "commit": "%E7%99%BB%E5%BD%95+Login",
        }
        # update_after_resp = requests.post("https://webvpn.hrbcu.edu.cn/users/sign_in", data=params, headers=headers)
        update_after_resp = session.post("https://webvpn.hrbcu.edu.cn/users/sign_in", data=params,  allow_redirects=False)
        print("update_after_resp.url: ", update_after_resp.url)

        print(update_after_resp.status_code)
        resp = session.get(update_url)
        print(resp.url)

    elif update_resp.url == "https://webvpn.hrbcu.edu.cn/":  # 登录成功.
        pass

    else:
        ValueError("Error, not match url. ")



def main2() -> None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
        "Referer": "https://webvpn.hrbcu.edu.cn/users/sign_in",
        "Host": "webvpn.hrbcu.edu.cn",
        "Origin": "https://webvpn.hrbcu.edu.cn",
        "Cookie": "SERVERID=Server1; _webvpn_key=; webvpn_username=; _astraeus_session=K0xITjJvL3ZMTXdzLzBXTlJISG96V0I5aXBqWUY2ZE9vc0VjWmFCWHdDdkZuNWJXc1N5eHdybFVJWjAyNmVRa2trdC9WcWl2emphYWtna1ZWc1ZTRjFGREo0TFNhMkhOUW5Bak45M1pUYm4xVFgrajFjK1JEYmFwbGdiZFprdmpJV2kvSU1haEVCSmJZNUlyalNjZ1VEREFYWFhjdmdtbVNhSXdkVE9BSUpDSmhxbFVJTjVteVVFRElYcS8xRFY0UTE0TnRWdEMrNVlMQlZvU0FraHZDaGF1VGtOTTlIT2VQYjR6cWRmNElLQ1ZiZ2lhZkRNbjVvL1pRMElhTzQ1V1VVdHZKSklGSnFzT28xb1RCVmQrU24rZmVHUDdrYjlLSWdOb29HOVBhRk5HclBRMWIzdkJVR2JneG9qUEhvcSsyTlVnYXVnb0hhS2EvQ0xVMXpqSlRCdXlFNklMQWFORE9semZuV0lheXVqZlJWYmN5VVBCTXhZTSsrWS9pMlRwc2xER3VEbGMzYkptQnhQcENuT05oRGJ4ZHVHQldmYlIyb1E0bWt4Qm5CdUNXWnB2RXlXbGRteHFFWjE3Z2VmQmNyMFlVV2lRbVR4RVBKVkJ2S0g2bk1CalNwOWNkSi9vVU1ZV0pucnRZWDA9LS1ZSTRRWm4yeGVQaW44OFR0aHpZM1BBPT0%3D--0e916460fd6a5c4521e59981e58ae841d7964980"
    }
    params = {
        # "utf8": "✓",
        # "authenticity_token": "4NyTdLLQnctPJUvgnSH9aXEaWDP6t2dBinfc67/xpPwhzx7HshS52iBRgOtWh9ZavmtFJHMVt7nYZvLSQREDLw==",
        # "user[login]": "201923020986",
        # "user[password]": "FWJ@15246337585",
        # "user[dymatice_code]": "unknown",
        # "user[otp_with_capcha]": "false",
        # "commit": "登录 Login",

        "utf8": "%E2%9C%93",
        "authenticity_token": "4NyTdLLQnctPJUvgnSH9aXEaWDP6t2dBinfc67%2FxpPwhzx7HshS52iBRgOtWh9ZavmtFJHMVt7nYZvLSQREDLw%3D%3D",
        "user%5Blogin%5D": "201923020986",
        "user%5Bpassword%5D": "FWJ%4015246337585",
        "user%5Bdymatice_code%5D": "unknown",
        "user%5Botp_with_capcha%5D": "false",
        "commit": "%E7%99%BB%E5%BD%95+Login",
    }

    sess = requests.Session()
    resp = sess.get(sign_in_url, params=params, headers=headers)
    print(resp.status_code)

    sign_in_resp_cookie = resp.headers["Set-cookie"].split("=")[1].split(";")[0]
    print(sign_in_resp_cookie)
    update_request_cookie = "SERVERID=Server1; _webvpn_key=; webvpn_username=; _astraeus_session="+sign_in_resp_cookie
    headers["Cookie"] = update_request_cookie
    final_resp = requests.get(update_url, headers=headers)
    print(final_resp.status_code)
    print(final_resp.url)



def main_selenium() -> None:
    options = webdriver.FirefoxOptions()
    options.headless = True  # 相当于执行了opt.add_argument('-headless')
    options.set_preference('permissions.default.image', 2)  # 禁止加载图片


    firefox = webdriver.Firefox(options=options)

    firefox.get(sign_in_url)

    firefox.find_element(By.ID,"user_login").send_keys(username)
    firefox.find_element(By.ID, "user_password").send_keys(passward)

    firefox.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()


    cookie = []
    for dic in firefox.get_cookies():
        cookie.append(dic["name"] + "=" + dic["value"])

    cookie = "; ".join(cookie).strip()
    print(cookie)

    firefox.quit()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
        "Referer": "https://webvpn.hrbcu.edu.cn/users/sign_in",
        "Host": "webvpn.hrbcu.edu.cn",
        "Cookie":cookie,
    }


    resp = requests.get(web_vpn_url, headers=headers)
    print(resp.status_code)
    print(resp.text)







if __name__ == '__main__':
    # main()
    # main2()
    main_selenium()