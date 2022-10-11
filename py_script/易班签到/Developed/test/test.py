import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions


def sign_in(users):
    UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"

    options = webdriver.EdgeOptions()

    mobileEmulation = {"deviceMetrics": {"width": 400, "height": 600, "pixelRatio": 0},
                       "userAgent": users["user_agent"]}

    # print(user["deviceName"], user["user_agent"])

    options.add_experimental_option('mobileEmulation', mobileEmulation)

    print(users["user_agent"])

    edge = webdriver.Edge(options=options)

    # url = r"https://app.uyiban.com/nightattendance/student/#/home?AppName=%E6%99%9A%E7%82%B9%E7%AD%BE%E5%88%B0"

    url = "https://c.uyiban.com/#/"
    edge.get(url)
    time.sleep(1)

    # 登录

    edge.find_element(By.ID, "oauth_uname_m").send_keys(users["phone"])
    edge.find_element(By.ID, "oauth_upwd_m").send_keys(users["password"])
    edge.find_element(By.CLASS_NAME, "oauth_check_login").click()

    time.sleep(1)
    # 点击网点签到
    # edge.find_element(By.CLASS_NAME, "am-flexbox interior___2LrxB am-flexbox-dir-column am-flexbox-align-center") # 点击晚点亲签到

    while 1:
        try:
            edge.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]").click()  # 点击任务反馈
            break
        except Exception:
            print("等待")

    while 1:
        try:
            time.sleep(0.5
                       )
            eles = edge.find_elements(By.CLASS_NAME, "content___3S97q") # 点击采集
            # print(len(list(eles)))
            i = 0
            print(len(eles),"len")
            for ele in eles:
                print(ele.get_attribute("outerHTML"))
                i += 1
                print(i)
            print(i,"out")
            #     print(ele.get_attribute("outerHTML"))
                # time.sleep(0.5)
                # ele.click()
                # time.sleep(0.5)
                # edge.back() # 返回

            break

        except Exception:
                print("2等待")

    input("paush")


# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div
# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[2]/div
# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[3]/div
...


# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[15]/div

def print_user(user):
    if isinstance(user, dict):
        for key, value in user.items():
            print(key, value, sep=":\t", end='\n')


def main():
    users = [
        {
            # FWJ个人信息
            "phone": "15246337585",
            "password": "fwj15246337585",
            "deviceName": "Galaxy s9",
            "cokkie": {
                "csrf_token": "40e8e234aca3582615dee9c01b2eb5f3",
            },
            # "user_agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Edg/95.0.4638.5",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"
            # 测试用

        },

        {
            # LZA个人信息
            "phone": "13845635041",
            "password": "lzajkluio0",
            "deviceName": "Galaxy s5",
            "cokkie": {
                "csrf_token": "40e8e234aca3582615dee9c01b2eb5f3",
            },
            # "user_agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Edg/95.0.4638.5",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"

        },

        {
            # JTY个人信息
            "phone": "13763749040",
            "password": "jitengyue200119",
            "deviceName": "Galaxy s5",
            "cokkie": {
                "csrf_token": "40e8e234aca3582615dee9c01b2eb5f3",
            },
            # "user_agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Edg/95.0.4638.5",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"

        }
    ]

    # print_user(users[0])
    sign_in(users[0])  # 单人测试

    # for user in users:
    #     sign_in(user)


if __name__ == '__main__':
    main()
