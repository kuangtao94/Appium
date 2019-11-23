from appium import webdriver
from time import sleep

descred_caps = {
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.baidu.yuedu",
    "appActivity":"com.baidu.yuedu.splash.SplashActivity",
    "noRset":"true",
    "unicodeKeyboard":"true", #打开软键盘输入中文
    "resetKeyboard":"true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",descred_caps)

#获取屏幕size
size = driver.get_window_size()
print(size)

#屏幕的宽度 width
print(size["width"])

#屏幕的高度 height
print(size["height"])

def swipeUp(driver,t=500,n=1):
    """向上屏幕滑动"""
    x1 = size["width"] * 0.5 # x坐标
    y1 = size["height"] * 0.75 # 起点 y坐标
    y2 = size["height"] * 0.25 # 终点 y 坐标
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeDown(driver,t=500,n=1):
    """向下屏幕滑动"""
    x1 = size["width"] * 0.5 # x1 坐标
    y1 = size["height"] * 0.25 # 起点y1坐标
    y2 = size["height"] * 0.75 # 终点y2坐标
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeLeft(driver,t=500,n=1):
    """向左屏幕滑动"""
    x1 = size["width"] * 0.75 # 起点x1坐标
    y1 = size["height"] * 0.5 # y1 坐标
    x2 = size["width"] * 0.25 # 终点x2坐标
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)

def swipeRight(driver,t=500,n=1):
    """向右屏幕滑动"""
    x1 = size["width"] * 0.25 #起点x1坐标
    y1 = size["height"] * 0.5 # y1坐标
    x2 = size["width"] * 0.75 #终点x2坐标
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)

if __name__ == "__main__":
    print(driver.get_window_size())
    sleep(5)
    swipeLeft(driver, n=2)
    sleep(2)
    swipeRight(driver, n=2)
    driver.quit()