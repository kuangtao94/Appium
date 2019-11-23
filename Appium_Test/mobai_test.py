from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '9',
                'deviceName': '4871660c',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Appium',
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# def swipeDown(driver,t=100,n=1):
#     """向下滑动屏幕"""
#     size = driver.get_window_size()
#     print(size)
#     x1 = size['width']*0.5
#     y1 = size['height']*0.25
#     y2 = size['height']*0.75
#     for i in range(n):
#         driver.swipe(x1,y1,x1,y2,t)
#
# swipeDown(driver)
# sleep(2)

sleep(3)
#打印屏幕宽和高
print(driver.get_window_size())
#获取屏幕的宽
x = driver.get_window_size()['width']
#获取屏幕的高
y = driver.get_window_size()['height']

#向下滑动
driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)
sleep(3)

#获取当前的会话
print(driver.contexts)

#点开小程序
driver.find_element_by_id("com.tencent.mm:id/jb")[1].click()
sleep(2)



