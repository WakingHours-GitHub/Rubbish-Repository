import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions


def sign_in(users):
    UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"

    options = webdriver.EdgeOptions()

    mobileEmulation = {"deviceMetrics": {"width": 400, "height": 600, "pixelRatio": 0}, "userAgent": users["user_agent"]}

    # print(user["deviceName"], user["user_agent"])

    options.add_experimental_option('mobileEmulation', mobileEmulation)

    print(users["user_agent"])

    edge = webdriver.Edge(options=options)

    # url = r"https://app.uyiban.com/nightattendance/student/#/home?AppName=%E6%99%9A%E7%82%B9%E7%AD%BE%E5%88%B0"

    url = "https://c.uyiban.com/#/"
    edge.get(url)
    time.sleep(1)

    # 登录
    
    edge.find_element(By.ID,"oauth_uname_m").send_keys(users["phone"])
    edge.find_element(By.ID,"oauth_upwd_m").send_keys(users["password"])
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

    for i in range(2,15):
        divXpath = "/html/body/div/div/div[1]/div[1]/div/div[3]/div/div["+ str(2) +"]/div"


        while 1:
            try:
                edge.find_element(By.XPATH, divXpath).click() # 点击第二个任务
                break
            except Exception:
                print("2等待")

        while 1:
            try:
                edge.find_element(By.XPATH, "/html/body/div/div/footer/a/span").click() # 点击反馈
                break
            except Exception:
                print("3等待")

        # 输入体温
        temp = random.randint(35, 36) + int(random.random()*10) /10  # 模拟体温

        while 1:
            try:
                edge.find_element(By.CLASS_NAME, "hx-form-input-input").send_keys(str(temp))
                break
            except Exception:
                print("4等待")

        # 点击是否在校园
        while 1:
            try:
                edge.find_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[2]").click()
                break
            except Exception:
                print("5等待")
        # 点击是
        while 1:
            try:
                edge.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[1]/label/div").click()
                time.sleep(0.2)
                edge.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[1]/a[2]").click()
                break
            except Exception:
                print("6等待")

        # 点击提交
        while 1:
            try:
                edge.find_element(By.XPATH, "/html/body/div/div/footer/a/span").click()
                # time.sleep(100)
                edge.back()
                edge.back()
                edge.refresh()
                # edge.back()
                break
            except Exception:
                print("6等待")










    time.sleep(100)

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
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4" # 测试用
                        
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
