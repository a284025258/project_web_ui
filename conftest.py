import pytest
from selenium import webdriver
from common.constant import constant
from pages.login import LoginPage
from pages.home import HomePage


@pytest.fixture(scope='class', autouse=True)
def init_web():
    # 启动浏览器
    driver = webdriver.Chrome(constant.DRIVER_PATH)
    # 窗口最大化
    driver.maximize_window()
    # 设置隐式等待
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


# @pytest.fixture()
# def set_up_refresh():
#     driver = init_web
#     driver.refresh()
