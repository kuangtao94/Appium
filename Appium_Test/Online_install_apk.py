import os
from appium import webdriver
# 安装app,为了方便，把app放到当前脚本同一目录
os.system("adb install sina.apk")

#获取项目的根目录路径
path_file = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
print(path_file)

#获取app的路径
# app_path = os.path.join(path_file,"apk","sina.apk")
app_path = lambda x : os.path.join(path_file,"app",x)
print(app_path("sina.apk"))

desired_caps = {
    "platformName":"Android",
    "platformVersion":"9",
    "deviceName":"4871660c",
    "automationName":"Uiautomator2",
    "noReset":True,
    "app":app_path("sina.apk"),
    "appPackage":"com.sina.mail.free",
    "appActivity":"com.sina.mail.controller.FreeEntryActivity",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)