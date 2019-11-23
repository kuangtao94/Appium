from appium import webdriver

import time as t

desired_caps = {
    "platformName":"Android",
    "platfromVersion":"5.1.1",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.baidu.yuedu",
    "appActivity":"com.baidu.yuedu.splash.SplashActivity"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#获取当前的Activity
ac = driver.current_activity
print(ac)

"""
wait_activity(self, activity, timeout, interval=1):

    等待指定的activity出现直到超时，interval为扫描间隔1秒

    即每隔几秒获取一次当前的activity
    
    android特有的

    返回的True 或 False

    :Agrs:

     - activity - 需等待的目标 activity

     - timeout - 最大超时时间，单位是s

     - interval - 循环查询时间

    用法:driver.wait_activity(‘.activity.xxx’,5,2)
"""
#等主页面activity出现,10s内
# driver.wait_activity(".splash.SplashActivity",30,1)

# #点击下次再说
# driver.find_element_by_id("com.baidu.yuedu:id/btn_cancel").click()
t.sleep(30)
#点击免费
driver.find_element_by_id("com.baidu.yuedu:id/community_title").click()
print(driver.contexts)

#获取当前的Activity
print(driver.current_activity)


