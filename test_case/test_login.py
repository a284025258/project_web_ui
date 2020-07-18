from selenium import webdriver
from unittest import TestCase
from common.constant import constant
from lib.ddt import ddt, data
from pages.home import HomePage
from pages.login import LoginPage
from data.login_data import login_data
import pytest


class TestLogin(object):
    """登录测试用例"""
    # @pytest.mark.usefixtures('set_up_refresh')
    @pytest.mark.parametrize('case', login_data)
    def test_login(self, case, init_web):
        driver = init_web
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        # 每次登录前刷新页面，清空输入框内容
        driver.refresh()
        login_page.login(case['username'], case['password'])
        # 断言
        try:
            # 获取实际结果
            element = None
            if 'success' in case['tags']:
                element = home_page.get_my_account_element()
            elif 'error' in case['tags']:
                element = login_page.get_error_element()
            elif 'alert' in case['tags']:
                element = login_page.get_invalid_element()
            assert case['expected'] == getattr(element, 'text')
            print('用例执行成功')
        except Exception as e:
            # 截图
            home_page.screen_shot()
            print('用例执行失败')
            raise e
