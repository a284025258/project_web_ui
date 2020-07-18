from common.config import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.locators import LoginPageLocator
from common.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""
    url = '/Index/login.html'

    def login(self, username: str, password: str):
        """登录"""
        # 访问目标网址
        self.driver.get(config.get('url', 'url') + self.url)
        # 获取手机号输入框元素定位
        element_phone = self.explicit_wait_visibility(LoginPageLocator.locator_phone)
        # 获取密码输入框元素定位
        element_pwd = self.explicit_wait_visibility(LoginPageLocator.locator_password)
        # 获取登录按钮元素定位
        # element_button = self.explicit_wait_clickable(LoginPageLocator.locator_submit)
        element_phone.send_keys(username)
        element_pwd.send_keys(password)
        # element_button.click()
        # 通过定位到 password 输入框 按回车登录
        self.enter(element_pwd)

    def get_error_element(self):
        """
        获取登录失败的提示 WebElement 对象
        :return: WebElement 对象
        """
        return self.explicit_wait_visibility(LoginPageLocator.locator_error)

    def get_invalid_element(self):
        """
            获取登录失败的弹窗提示 WebElement 对象
            :return: WebElement 对象
        """
        return self.explicit_wait_visibility(LoginPageLocator.locator_invalid)
