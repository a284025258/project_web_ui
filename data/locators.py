"""
所有页面 locator 类
"""
from selenium.webdriver.common.by import By


class CommonPage(object):
    # 我的账户
    locator_my_account = (By.XPATH, '//a[@href="/Member/index.html"]')
    # 退出
    locator_logout = (By.XPATH, '//a[@href="/Index/logout.html"]')


class LoginPageLocator(object):
    """登录页面常用元素定位器"""
    # 电话号码输入框
    locator_phone = (By.NAME, 'phone')
    # 密码输入框
    locator_password = (By.NAME, 'password')
    # 提交按钮
    locator_submit = (By.CLASS_NAME, 'btn-special')
    # 输入框提示
    locator_error = (By.CLASS_NAME, 'form-error-info')
    # 弹窗提示
    locator_invalid = (By.CLASS_NAME, 'layui-layer-content')


class HomePageLocator(object):
    """主页页面常用元素定位器"""
    # 我的账户
    locator_my_account = (By.XPATH, '//a[@href="/Member/index.html"]')
    # 退出
    locator_logout = (By.XPATH, '//a[@href="/Index/logout.html"]')
    # 抢投标
    locator_bid_button = (By.XPATH, '(//div[@class="text-center"]/a)[1]')


class BidPageLocator(object):
    """投标详情页页面常用元素定位器"""
    # 可用余额
    locator_available_balance = (By.CLASS_NAME, 'invest-unit-investinput')
    # 投标按钮
    locator_bid_button = (By.CLASS_NAME, 'height_style')
    locator_bid_success = (By.XPATH, "//div[@class='layui-layer-content']/div[@class='capital_ts']/div[contains(@class, 'note')]")
    locator_view_activate = (By.XPATH, "//div[@class='layui-layer-content']/div[@class='capital_ts']/div/button")
