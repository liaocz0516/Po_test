"""
   步骤：
        1. 新建页面类
        2.将每一步业务操作进行单独封装
        3.添加组合业务方法
"""
# unittest 执行页
import unittest
from page_ymdx.page import pagelogin


class TTXC_Unittest(unittest.TestCase):
    def setUp(self):
        # 实例化 page.py 中 pagelogin 对象
        self.login = pagelogin()

    # 参数化
    def test1_login(self, username="15970771067", pwd="qwer123"):
        self.login.page_login(username, pwd)
