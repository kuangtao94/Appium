# coding:utf-8
from appium import webdriver
from time import sleep

desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '5.1.1',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
                'noReset': 'true',
                'resetKeyboard': 'true',
                'unicodeKeyboard': 'true'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 等主页面activity出现
driver.wait_activity(".base.ui.MainActivity", 10)

# 1.text
loc_text = 'new UiSelector().text("图书")'
driver.find_element_by_android_uiautomator(loc_text).click()

# # 2.textContains
# loc_textContains = 'new UiSelector().textContains("图")'
# driver.find_element_by_android_uiautomator(loc_textContains).click()

# # 3.textStartsWith
# loc_textStart = 'new UiSelector().textStartsWith("图")'
# driver.find_element_by_android_uiautomator(loc_textStart).click()

sleep(2)
# resourceId定位'小说'
loc_id = 'new UiSelector().resourceId("com.baidu.yuedu:id/webbooktitle")'
driver.find_element_by_android_uiautomator(loc_id).click()

sleep(2)
# className复数定位
loc_class = 'new UiSelector().className("android.widget.TextView")'
driver.find_elements_by_android_uiautomator(loc_class)[2].click()



"""
https://www.cnblogs.com/yoyoketang/p/7833554.html
1.通过text文本定位语法
new UiSelector().text("text文本")

2.文本比较长的时候，可以用textContains模糊匹配,只要文本包含匹配内容就可以了。
new UiSelector().textContains("包含text文本")

3.textStartsWith是以某个文本开头的匹配
new UiSelector().textStartsWith("以text文本开头")

4.正则匹配textMatches，这个需要配合正则表达式，就不举例了。
new UiSelector().textMatches("正则表达式")

5.resourceId根by_id一样
new UiSelector().resourceId("id")

6.页面上的class属性一般不唯一，多半用在复数定位时候。
比如通过class属性定位'排行'这个按钮下标就是2。
new UiSelector().className("className")

7.由于这个app的contenet-des属性都是空的，就不用代码演示了，跟上面方法一样。
new UiSelector().description("contenet-des属性")
"""