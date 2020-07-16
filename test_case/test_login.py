from selenium import webdriver
from unittest import TestCase
from common.constant import constant
from common.config import config
from common.read_excel import ReadExcel
import os
from lib.ddt import ddt, data
from common.text_replace import data_replace


def login(driver, username, password):
    """登录"""
    # 访问目标网址
    driver.get(config.get('url', 'url') + '/Index/login.html')
    # 获取手机号输入框元素定位
    element_phone = driver.find_element_by_name('phone')
    # 获取密码输入框元素定位
    element_pwd = driver.find_element_by_name('password')
    # 获取登录按钮元素定位
    element_button = driver.find_element_by_css_selector("[type='button']")
    element_phone.send_keys(username)
    element_pwd.send_keys(password)
    element_button.click()


@ddt
class TestLogin(TestCase):
    """登录测试用例"""
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        # 启动浏览器
        self.driver = webdriver.Chrome(constant.DRIVER_PATH)
        # 窗口最大化
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(constant.TIMEOUT)

    def tearDown(self) -> None:
        self.driver.quit()

    read_excel = ReadExcel(os.path.join(constant.DATA_DIR, 'cases.xlsx'), 'login')
    cases = read_excel.read_data_obj()

    @data(*cases)
    def test_login(self, case):
        login(self.driver, eval(data_replace(case.data))['username'], eval(data_replace(case.data))['password'])
        # 获取实际结果
        result = self.driver.find_element_by_class_name('form-error-info').text
        # 断言
        try:
            self.assertEqual(case.assert_expect, result)
            print('用例执行成功')
        except Exception as e:
            print('用例执行失败')
            raise e
