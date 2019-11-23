from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep

#apk 路径
PATH = lambda x : os.path.join(os.path.dirname(os.path.realpath(__file__)),x)

#百度下载开发者头条，放在当前脚本目录
print(PATH("toutiao.apk"))

desired_caps = {
    "platformName":"Android",
    "platformVersion":"9",
    "deviceName":"4871660c",
    "app":PATH("toutiao.apk"),
    "appPackage":"io.manong.developerdaily",
    "appActivity":"io.toutiao.android.ui.activity.LaunchActivity",
    "noReset":True,
    "autoAcceptAlerts":"true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

sleep(3)
#打印屏幕宽和高
print(driver.get_window_size())
#获取屏幕的宽
x = driver.get_window_size()['width']
#获取屏幕的高
y = driver.get_window_size()['height']

# sleep(2)
# def swipe_right(driver,n=None):
    # return:实现从右到左滑动,滑动时X轴起点小于终点
    # x1 = size["width"] * 0.75  # 起点x1坐标
    # y1 = size["height"] * 0.5  # y1 坐标
    # x2 = size["width"] * 0.25  # 终点x2坐标
    # for i in range(n):
    #     sleep(1)
    #     # driver.swipe(x1, y1, x2, y1, t)
    #     driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 100)

def always_allow(driver,number=1,n=3):
    """
    :param driver: function 权限弹窗默认允许 -- 传driver
    :param number: 判断弹窗次数，默认5次
    WebDriverWait 里面0.5s判断一次是否有弹窗，1s超时
    """
    for i in range(number):
        loc = ("xpath","//*[@text='允许']")
        # id_text = 'resourceId("android:id/button1").text("允许")'
        try:
            # WebDriverWait(driver,1,0.5).until(EC.presence_of_element_located(loc)).click()
            driver.switch_to_alert()
            sleep(1)
            driver.switch_to.alert.accept()
            #return:实现从右到左滑动,滑动时X轴起点小于终点
            for i in range(n):
                sleep(1)
                # driver.swipe(x1, y1, x2, y1, t)
                driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 100)
        except:
            print("Error")


if __name__ == "__main__":
    # 调用始终允许函数
    always_allow(driver)
    # size = driver.get_window_size()
    # swipe_right(driver,n=3)
