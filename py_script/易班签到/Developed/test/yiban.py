import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def sign_in(users):
    for user in users:
        print(f"当前执行的是：用户：{user['phone']}")
        options = webdriver.EdgeOptions()
        mobileEmulation = {"deviceMetrics": {"width": 400, "height": 600, "pixelRatio": 0},
                           "userAgent": user["user_agent"]}

        options.add_experimental_option('mobileEmulation', mobileEmulation)

        edge = webdriver.Edge(options=options)

        url = "https://c.uyiban.com/#/"
        edge.get(url)
        # 登录
        # input框, 利用send_keys输入内容
        while True:
            try:
                edge.find_element(By.ID, "oauth_uname_m").send_keys(user["phone"])
                edge.find_element(By.ID, "oauth_upwd_m").send_keys(user["password"])
                edge.find_element(By.CLASS_NAME, "oauth_check_login").click()

                break
            except Exception:

                print("没有登录")

        # 点击任务反馈
        while True:
            try:
                edge.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]").click()  # 点击任务反馈
                break
            except Exception:
                print("等待")

        while True:
            try:
                time.sleep(0.5)
                eles = edge.find_elements(By.CLASS_NAME, "content___3S97q")  # 获取采集信息的可迭代对象。
                f = len(eles)

                for i in range(f):
                    # 每次点击第一个采集div
                    while 1:
                        try:
                            # /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div
                            edge.find_element(By.XPATH,
                                              "/html/body/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div").click()
                            break
                        except Exception:
                            print("2等待")

                    # edge.back() # 单次模拟
                    time.sleep(0.5)  # 缓冲

                    # 点击反馈
                    while 1:
                        try:
                            edge.find_element(By.XPATH, "/html/body/div/div/footer/a/span").click()  # 点击反馈
                            break
                        except Exception:
                            print("3等待")

                    # 输入体温
                    temp = random.randint(35, 36) + int(random.random() * 10) / 10  # 模拟体温

                    while 1:
                        try:
                            # edge.find_element(By.CLASS_NAME, "hx-form-input-input").send_keys(str(temp))
                            edge.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/input").send_keys(
                                str(temp))  # 使用XPATH寻找元素
                            break
                        except Exception:
                            print("4等待")
                    # 点击是否在校园中的模块
                    while 1:
                        try:
                            edge.find_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[2]").click()
                            break
                        except Exception:
                            print("5等待")
                    time.sleep(0.2)
                    # 点击是：在校园
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

                edge.quit()  # 退出浏览器
                print(f"{user['phone']}用户已经完成")

                break
            except Exception:
                print("没找到任务列表")
    print("所有用户已经完成")


# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div
# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[2]/div
# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[3]/div
# ...

# /html/body/div/div/div[1]/div[1]/div/div[3]/div/div[15]/div

def print_user(user):
    if isinstance(user, dict):
        for key, value in user.items():
            print(key, value, sep=":\t", end='\n')


def main():
    users = [
        {
            # WH个人信息
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
            # 老刘个人信息
            "phone": "13845635041",
            "password": "lzajkluio0",
            "deviceName": "HUAWEI",
            "cokkie": {
                "csrf_token": "40e8e234aca3582615dee9c01b2eb5f3",
            },
            # "user_agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Edg/95.0.4638.5",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"
        },

        {
            # 老纪个人信息
            "phone": "13763749040",
            "password": "jitengyue200119",
            "deviceName": "HUAWEI",
            "cokkie": {
                "csrf_token": "40e8e234aca3582615dee9c01b2eb5f3",
            },
            # "user_agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Edg/95.0.4638.5",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.4"

        }
    ]
    # print_user(users[0])
    # sign_in(users[0])  # 单人测试

    sign_in(users)  # 多人测试


if __name__ == '__main__':
    main()
