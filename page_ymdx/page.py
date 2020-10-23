"""存放页面对象"""

# 导入base_ggff包
from base_ggff.base import Base
from selenium.webdriver.common.by import By

# 公共方法
username = [By.CSS_SELECTOR, "[placeholder='请输入账号名称']"]
password = [By.CSS_SELECTOR, "[placeholder='请输入账号密码']"]
login_button = [By.CSS_SELECTOR, "[class='btn active']"]

'''使用继承的方式引用base中的方法，不需要实例化对象'''
class pagelogin(Base):
    # 1. 用户名
    def page_input_username(self, username_value):
        self.base_input(username, username_value)

    # 2. 密码
    def page_input_password(self, pwd):
        self.base_input(password, pwd)

    # 3. 登录按钮
    def page_click_btn(self):
        self.base_click(login_button)

    # 4. 组合业务层
    def page_login(self, user_name, password_value):
        # 此处的用户名,密码 取名需要做区分，因为上方有全局变量，避免变量重复
        self.page_input_username(user_name)
        self.page_input_password(password_value)
        self.page_click_btn()
