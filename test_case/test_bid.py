from selenium import webdriver
from unittest import TestCase
from common.constant import constant
from lib.ddt import ddt, data
from pages.home import HomePage
from pages.login import LoginPage
from pages.bid import BidPage
from data.bid_data import bid_data
from common.config import config
import time
import pytest


class TestBid(object):
    """投标测试用例"""
    @pytest.mark.parametrize('case', bid_data)
    def test_bid(self, case, init_web):
        driver = init_web
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        bid_page = BidPage(driver)
        # 登录
        login_page.login(config.get('data', 'phone'), config.get('data', 'password'))
        # 断言
        try:
            # 确认首页已经打开
            home_page.opened()
            # 首页，点击投标，进入投标详情页
            home_page.get_bid_button().click()
            # 投标详情页，定位可用余额输入框
            element_available_balance = bid_page.get_available_balance()
            element_available_balance.send_keys(case['amount'])
            # 投标详情页，定位投标按钮
            element_bid_button = bid_page.get_bid_button()
            # 断言
            assert case['expected'] == getattr(element_bid_button, 'text')
            print('用例执行成功')
        except Exception as e:
            # 截图
            home_page.screen_shot()
            print('用例执行失败')
            raise e
