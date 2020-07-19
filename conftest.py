import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from common.constant import constant


@pytest.fixture(scope='class', autouse=True)
def init_web():
    # 设置无头浏览器
    chrome_options = ChromeOptions()
    chrome_options.binary_location = r'C:\Users\LittleStone\AppData\Local\Google\Chrome\Application\chrome.exe'
    # 启动浏览器
    driver = webdriver.Chrome(constant.DRIVER_PATH, options=chrome_options)
    # 窗口最大化
    driver.maximize_window()
    # 设置隐式等待
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# @pytest.fixture()
# def set_up_refresh():
#     driver = init_web
#     driver.refresh()
