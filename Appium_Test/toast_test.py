# # coding:utf-8
# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# desired_caps = {
#                 'platformName': 'Android',
#                 'deviceName': '127.0.0.1:62001',
#                 'platformVersion': '5.1.1',
#                 'appPackage': 'com.baidu.yuedu',
#                 'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
#                 'noReset': 'true',
#                 'automationName': 'Uiautomator2'
#                 }
#
# #装判断是否存在toast消息，存在返回True,不存在返回False
# def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
#     '''is toast exist, return True or False
#     :Agrs:
#      - driver - 传driver
#      - text   - 页面上看到的文本内容
#      - timeout - 最大超时时间，默认30s
#      - poll_frequency  - 间隔查询时间，默认0.5s查询一次
#     :Usage:
#      is_toast_exist(driver, "看到的内容")
#     '''
#     try:
#         toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
#         WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
#         # 定位toast元素
#         toast_loc = ("xpath", ".//*[contains(@text,'再按一次退出')]")
#         print(WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc)))
#         return True
#     except:
#         return False
#
# if __name__ == "__main__":
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#     # 等主页面activity出现
#     driver.wait_activity(".base.ui.MainActivity", 10)
#
#     driver.back()   # 点返回
#
#     # 判断是否存在toast-'再按一次退出'
#     print (is_toast_exist(driver, "再按一次退出"))



from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '5.1.1',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
                'noReset': 'true',
                'automationName': 'Uiautomator2'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 等主页面activity出现
driver.wait_activity(".base.ui.MainActivity", 10)

print(driver.current_activity)
print(driver.contexts)

remen = driver.find_elements_by_class_name("android.widget.LinearLayout")
print([item for item in remen])
print(type(remen))
driver.find_element_by_xpath("//android.widget.CheckBox[@text = '文学艺术']").click()
driver.find_element_by_xpath("//android.widget.CheckBox[@text = '历史']").click()
driver.find_element_by_xpath("//*[@text = '选好了']").click()

driver.back()   # 点返回
# 定位toast元素
toast_loc = ("xpath", ".//*[contains(@text,'再按一次退出')]")
print(WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc)))