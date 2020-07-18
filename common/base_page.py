from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from common.logger import log
import os
from common.constant import constant
import time
import win32gui
import win32con


class BasePage(object):
    """页面对象父类"""
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.action = ActionChains(self.driver)

    def screen_shot(self):
        """
        截图
        :return:
        """
        self.driver.save_screenshot(os.path.join(constant.SCREENSHOTS_DIR, time.strftime(
            "[%Y-%m-%d] [%H-%M-%S]", time.localtime()) + '.png'))

    def explicit_wait_visibility(self, locator: tuple):
        """
        显示等待--直到元素可见
        :param locator: 元素定位器
        :return: WebElement 对象
        """
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException as e:
            log.exception(e)
            self.screen_shot()

    def explicit_wait_clickable(self, locator: tuple):
        """
        显示等待--直到元素可被点击
        :param locator: 元素定位器
        :return: WebElement 对象
        """
        try:
            return self.wait.until(ec.element_to_be_clickable(locator))
        except TimeoutException as e:
            log.exception(e)
            self.screen_shot()

    def explicit_wait_presence(self, locator: tuple):
        """
        显示等待--直到元素出现
        :param locator: 元素定位器
        :return: WebElement 对象
        """
        try:
            return self.wait.until(ec.presence_of_element_located(locator))
        except TimeoutException as e:
            log.exception(e)
            self.screen_shot()

    def right_click(self, element):
        """
        鼠标右击
        :param element:
        :return:
        """
        return self.action.context_click(element).perform()

    def move_to(self, element):
        """
        鼠标移动
        :param element:
        :return:
        """
        return self.action.move_to_element(element).perform()

    def enter(self, element):
        """
        回车
        :param element:
        :return:
        """
        return element.send_keys(Keys.ENTER)

    def upload(self, element, path):
        element.click()
        time.sleep(1)
        # 打开一级窗口
        dialog = win32gui.FindWindow('#32770', '打开')
        # 二级窗口
        comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, 'ComboBox', None)
        # 四级窗口
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
        # 打开
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        time.sleep(1)
        # 选中文件
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, path)
        time.sleep(1)
        # 单击打开，选择文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
