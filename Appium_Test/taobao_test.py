# -*- coding：gbl8030 -*-
from appium import webdriver
import time as t
from appium.webdriver.common.mobileby import By


desired_caps = {
    "platformName":"Android",
    "platfromVersion":"5.1.1",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"io.manong.developerdaily",
    "appActivity":"io.manong.developerdaily/io.toutiao.android.ui.activity.LaunchActivity",
    # "unicodeKeyboard":True, #屏蔽软键盘
    # "reseKeyboard":True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)

t.sleep(20)
driver.find_element_by_id("com.taobao.taobao:id/yes").click()
print(driver.contexts)
t.sleep(20)
#点击等待
driver.find_element_by_id("android:id/button2").click()
t.sleep(60)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
t.sleep(20)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
t.sleep(20)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("衣服")
t.sleep(20)
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()



