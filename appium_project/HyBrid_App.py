# HyBrid混合应用App测试

from appium import webdriver
from time import sleep

desired_caps = {
        'deviceName':'Android Emulator',
        'automationName':'Appium',
        'platformName':'Android',
        'platformVersion':'7.0',
        'appPackage':'com.example.anwebview',
        'appActivity':'.MainActivity',
}

driver = webdriver.Remote('http://localhost:4732/wd/hub',desired_caps)

#获取当前上下文
context = driver.current_context
# print(context)

#获取所有上下文
all_context = driver.contexts
for context in all_context:
    print(context)

#切换上下文
driver.switch_to.context('WEBVIEW_com.example.anwebview')

#进入webview模式进行操作
driver.find_element_by_id('index-kw').send_keys('appium mobile web')
driver.find_element_by_id('index-bn').click()
sleep(5)

driver.quit()