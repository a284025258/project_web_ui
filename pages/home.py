from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.locators import HomePageLocator
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from common.base_page import BasePage


class HomePage(BasePage):
    """主页页面"""
    title = '业内领先的社群互联网金融平台'

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

    def get_bid_button(self):
        return self.explicit_wait_clickable(HomePageLocator.locator_bid_button)

    def opened(self):
        """
        确认页面是否已经打开，判断标题是否包含title参数
        :return:
        """
        return self.wait.until(ec.title_contains(self.title))

    # def get(self, url):
    #     """
    #     设置网页超时时间并停止当前网页加载
    #     :param url: 当前网页 url
    #     :return:
    #     """
    #     try:
    #         self.driver.set_page_load_timeout(3)
    #         self.driver.get(url)
    #     except TimeoutException:
    #         # 终止网页加载
    #         self.driver.execute_script('window.stop()')
    #     finally:
    #         self.driver.set_page_load_timeout(-1)
