"""
    存放所有page页面公共方法
    Po 分层 公共方法抽取，适用于所有web自动化项目
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://studyo.yufengtek.com/admin/#/login')
        # self.driver.maximize_window()

    # 1. 查找元素方法 封装
    def base_find(self, loc):
        """
         显示等待
           参数解释：timeout（等待时间）；poll_frequency（访问频率）；
           x 表示 self.driver
        :param loc: 一个变量
        :return: 返回一个元素
        """
        # return 返回查找到的元素
        return WebDriverWait(self.driver,
                             timeout=10,
                             poll_frequency=0.5).until(lambda x: x.find_element(*loc))

    # 2. 输入方法 封装
    def base_input(self, loc, value):
        # 1. 获取元素 get element
        el = self.base_find(loc)
        # 2. 清空内容
        el.clear()
        # 3, 输入内容
        el.send_keys(value)

    # 3. 点击方法 封装
    def base_click(self, loc):
        self.base_find(loc).click()
