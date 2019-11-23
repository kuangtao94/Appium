from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
import os

desired_caps = {
    "platformName":"Android",
    "platformVersion":"9",
    "deviceName":"4871660c",
    "appPackage":"com.tencent.mm",
    "appActivity":".ui.LauncherUI",
    # "chromeOptions":"{'androidProcess':'com.tencent.mm:tools'}",
    "automationName":"Uiautomator2",
    # "unicodeKeyboard":True,
    # "resetKeyboard":True,
    "noReset":True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)

# 定位聊天记录列表，选第一个长按
e1 = driver.find_elements_by_id("com.tencent.mm:id/b6e")[0]
print(driver.page_source)

# 长按
TouchAction(driver).long_press(e1).perform()
time.sleep(3)

# 定位选项框‘删除该聊天’
driver.find_element_by_xpath("//*[@text='删除该聊天']").click()
time.sleep(3)

# 定位选项框‘取消’
driver.find_element_by_id("com.tencent.mm:id/azz").click()