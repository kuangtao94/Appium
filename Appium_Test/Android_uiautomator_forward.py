# coding:utf-8

"""https://www.cnblogs.com/yoyoketang/p/7843819.html"""

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '4.4.2',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
                'noReset': 'true',
                'resetKeyboard': 'true',
                'unicodeKeyboard': 'true'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 等主页面activity出现
driver.wait_activity(".base.ui.MainActivity", 10)

# 1.id+text
id_text = 'resourceId("com.baidu.yuedu:id/webbooktitle").text("小说")'
driver.find_element_by_android_uiautomator(id_text).click()

sleep(2)
# 2.class+text
class_text = 'className("android.widget.TextView").text("图书")'
driver.find_element_by_android_uiautomator(class_text).click()

sleep(2)
# 父子关系childSelector
son = 'resourceId("com.baidu.yuedu:id/rl_tabs").childSelector(text("小说"))'
driver.find_element_by_android_uiautomator(son).click()

sleep(2)
# 兄弟关系fromParent
brother = 'resourceId("com.baidu.yuedu:id/lefttitle").fromParent(text("图书"))'
driver.find_element_by_android_uiautomator(brother).click()

sleep(2)
# resourceIdMatches(".*xxx$")
idMatches = 'resourceIdMatches(".*id/lefttitle$")'
driver.find_element_by_android_uiautomator(idMatches).click()

sleep(2)
# classNameMatches(".*xxx$")
classMatches = 'classNameMatches(".*TextView$").text("小说")'
driver.find_element_by_android_uiautomator(classMatches).click()