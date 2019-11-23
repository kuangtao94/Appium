from TestCase.App_Po.base.BasePage import BasePage
from time import sleep

class PageItest(BasePage):
    #元素定位实例化属性
    input_username_text_loc = ('xxxxx')  # 输入账号
    input_password_text_loc = ('xxxxx')  # 输入密码
    click_login_button_loc = ('登录') # 点击登录
    login_success_info_loc = ('xxxx') # 获取登录成功后的断言信息
    login_error_info_loc = ('xxxxx') # 获取登录失败的断言信息

    #输入账号封装
    def input_username(self,username):
        self.by_id(self.input_username_text_loc).send_keys(username)

    #输入密码封装
    def input_password(self,password):
        self.by_id(self.input_password_text_loc).send_keys(password)

    #点击登录封装
    def click_login(self):
        self.by_name(self.click_login_button_loc).click()

    #获取登录成功后的断言文本
    def login_success(self):
        return self.by_id(self.login_success_info_loc).text

    #获取登录失败的断言文本
    def login_error(self):
        return self.by_id(self.login_error_info_loc).text

    #登录ITest流程封装
    def Itest_login_liucheng(self,username,password):
        sleep(2)
        self.input_username(username)
        self.input_password(password)
        self.click_login()