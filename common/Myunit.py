#测试固件分离

from TestCase.App_Po.page.Page_login import PageItest
from appium import webdriver
from time import sleep
import unittest
import os

class myunit(unittest.TestCase):
    sleep(60) #强制等待60s左右,避免用例跑起来失败
    def setUp(self) -> None:
        # apk 路径
        PATH = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

        # 下载itest
        print(PATH("iTest4.7.0.apk"))

        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "127.0.0.1:62001",
            "app": PATH("toutiao.apk"),
            "appPackage": "iflytek.testTech.propertytool",
            "appActivity": "iflytek.testTech.propertytool.activity.BootActivity",
            "noReset": True,
            "autoAcceptAlerts": "true",
            'unicodeKeyboard':True, #使用unicode编码发送字符串
            'resetKeyboard':True #将软键盘藏起来
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        #等待app首页出现
        self.driver.wait_activity('xxxxxxx',20)
        #实例化对象
        self.ITest = PageItest(self.driver)

    def tearDown(self) -> None:
        self.driver.close_app()
