import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# 创建Firefox选项对象并将配置文件对象传递给它
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")


user = 'handuck'
password = '51349924'


def cashmining_browser():
    """
    启动浏览器
    :return:
    """
    browser.get("https://cashmining.me/")
    lk2r()
    try:
        login_header = browser.find_element(By.XPATH, '//*[@data-target="#login_box"]').text
        if login_header == "Login":
            print("加载完成")

        else:
            print("加载失败")
            cashmining_browser()
    except:
        print("加载失败")
        cashmining_browser()


def lk2r():
    try:
        browser.find_element(By.XPATH, '//*[@id and @href and @target and @style="display: block; height: inherit;"]')
        print("发现广告")
        action.move_by_offset(30, 30).click().perform()
        time.sleep(3)
        all_windows = browser.window_handles
        # 如果有新窗口打开，则切换到新窗口并关闭它
        if len(all_windows) > 1:
            for window in all_windows:
                if window != main_window:
                    browser.switch_to.window(window)
                    browser.close()
                    # 切换回主窗口
                    browser.switch_to.window(main_window)
    except:
        pass


def login_stade():
    """
    登录浏览器
    :return:
    """
    lk2r()
    try:
        login_header = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/h1').text
        if login_header == "User Login":
            print("登入窗口加载成功")
        else:
            print("登入窗口加载失败")
            login_browser()
    except:
        print("登入窗口加载失败")
        login_browser()


def login_ac():
    lk2r()
    try:
        login_header = browser.find_element(By.XPATH, '//*[@href="?page=passive earning"]').text
        if login_header == "Passive Earning":
            print("登录成功")
        else:
            print("登录失败")
            cashmining_browser()

    except:
        print("登录失败")
        cashmining_browser()


def login_browser():
    lk2r()
    browser.find_element(By.XPATH, '//*[@data-target="#login_box"]').click()
    print("启动登录窗口")
    time.sleep(5)
    login_stade()
    lk2r()
    browser.find_element(By.XPATH, '//*[@name="user"]').send_keys(user)
    print("输入用户名")
    time.sleep(1)
    lk2r()
    browser.find_element(By.XPATH, '//*[@name="password"]').send_keys(password)
    print("输入密码")
    time.sleep(1)
    lk2r()
    browser.find_element(By.XPATH, '//*[@name="remember"]').click()
    print("点击记住密码")
    time.sleep(1)
    lk2r()
    browser.find_element(By.XPATH, '//*[@name="connect"]').click()
    print("点击登录")
    time.sleep(10)
    login_ac()


def mining_browser():
    lk2r()
    browser.find_element(By.XPATH, '//*[@href="?page=passive earning"]').click()
    print("点击mining页面")
    browser.get('https://cashmining.me/mining.php')

def mining_page():
    try:
        mining_url = browser.current_url
        if 'mining.php' in mining_url:
            print("冲浪页面加载成功")
            time.sleep(5)
            previous_url = ''
            while True:
                percent = get_progress_percentage(browser)
                while percent < 100:
                    print_progress_bar(percent)
                    percent = get_progress_percentage(browser)
                    time.sleep(0.1)
                print_progress_bar(100)
                print('\n')
                time.sleep(30)
                current_url = browser.current_url
                if 'mining.php' in current_url:
                    print('进入下一个页面...')
                    print(current_url)
                else:
                    break
                if current_url != previous_url:
                    previous_url = current_url
                else:
                    print('已达到最后一个页面')
                    break
        else:
            print("冲浪页面加载失败")
            browser.save_screenshot('mining_page.png')
    except:
        print("冲浪页面加载失败")
        browser.save_screenshot('mining_page.png')


def get_progress_percentage(browser):
    progress_bar = browser.find_element(By.CSS_SELECTOR, '.progress-bar')
    style = progress_bar.get_attribute('style')
    match = re.search(r'width:\s*([\d\.]+)%', style)
    if match:
        percent = float(match.group(1))
        return percent
    else:
        return None


def print_progress_bar(percent):
    width = 50
    filled_width = int(width * percent / 100)
    remaining_width = width - filled_width
    bar = '=' * filled_width + '-' * remaining_width
    print(f'[{bar}] {percent:.2f}%', end='\r')


if __name__ == '__main__':
    run = True
    while run:
        browser = driver = webdriver.Chrome(options=options)
        action = ActionChains(browser)
        wait = WebDriverWait(browser, 10)
        main_window = browser.current_window_handle
        cashmining_browser()
        login_browser()
        mining_browser()
        mining_page()
        browser.quit()
        print('系统错误等待10秒重试')
        time.sleep(10)
