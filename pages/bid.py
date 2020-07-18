from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.locators import BidPageLocator
from data.locators import HomePageLocator
from common.base_page import BasePage


class BidPage(BasePage):
    """投标详情页页面"""

    def get_my_account_element(self):
        """
        获取我的账户元素 WebElement 对象
        :return: WebElement 对象
        """
        return self.explicit_wait_visibility(HomePageLocator.locator_my_account)

    def get_logout_element(self):
        """
        获取帐号信息元素 WebElement 对象
        :return: WebElement 对象
        """
        return self.explicit_wait_visibility(HomePageLocator.locator_logout)

    def get_available_balance(self):
        """
        获取可用余额元素 WebElement 对象
        :return:
        """
        return self.explicit_wait_visibility(BidPageLocator.locator_available_balance)

    def get_bid_button(self):
        """
        获取投标按钮元素 WebElement 对象
        :return:
        """
        return self.explicit_wait_visibility(BidPageLocator.locator_bid_button)

    def get_bid_success(self):
        """
        获取投标成功元素 WebElement 对象
        :return:
        """
        return self.explicit_wait_visibility(BidPageLocator.locator_bid_success)

    def get_view_activate(self):
        """
        获取查看并激活按钮元素 WebElement 对象
        :return:
        """
        return self.explicit_wait_clickable(BidPageLocator.locator_view_activate)
