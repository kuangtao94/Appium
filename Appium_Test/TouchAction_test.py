from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from time import sleep

"""
class TouchAction(object):
    def __init__(self, driver=None):
        self._driver = driver
        self._actions = []

    def tap(self, element=None, x=None, y=None, count=1):
        模拟手指触摸屏

    def press(self, el=None, x=None, y=None):
        短按：模拟手指按住一个元素，或者坐标

    def long_press(self, el=None, x=None, y=None, duration=1000):
        长按：模拟按住一个元素，或者坐标

    def wait(self, ms=0):
        按住元素后的等待时间

    def move_to(self, el=None, x=None, y=None):
        移动手指到另外一个元素，或者坐标，注意这里坐标不是绝对坐标，是偏移量
        
    def release(self):
        释放手指

    def perform(self):
        执行前面的动作
        
MultiAction是针对多点触控操作的，是TouchAction的一个补充模块
多点触摸对象是触摸动作的集合。
多点触控手势只有两种方法，即添加和执行。
add用于添加另一个触摸操作到多点触摸。
当perform执行被调用时，添加到多点触摸的所有触摸动作都被发送到AppII，并执行，就像它们同时发生一样。appium首先执行所有触摸动作的第一个事件，然后执行第二个，等等。
"""

# el是定位元素的对象

# action0 = TouchAction().tap(el)
# action1 = TouchAction().tap(el)
# MultiAction().add(action0).add(action1).perform()

desired_caps = {
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.android.settings",
    "appActivity":"com.android.settings/.Settings",
    "noReset":"true",
    "unicodeKeyboard":"true",
    'resetKeyboard': 'true'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#点击搜索
driver.find_element_by_id("com.android.settings:id/search").click()
driver.find_element_by_id("android:id/search_src_text").send_keys("安全\n")
driver.find_elements_by_id("android:id/search_src_text")[0].click()

#屏幕安全保护
driver.find_element_by_id("android.widget.RelativeLayout").click()
driver.find_element_by_xpath("//*[@text = '图案']").click()

sleep(5)
#解决问题思路：先获取元素坐标位置，再获取元素大小，然后切割图片，分别计算出每个点的坐标
#定位九宫格元素
jiu = 'resourceId("com.android.settings:id/lockPattern").index(2)'
local = driver.find_element_by_android_uiautomator(jiu).location
print("获取九宫格坐标位置:%s"%local)

s = driver.find_element_by_android_uiautomator(jiu).size
print("获取九宫格宽和高:%s"%s)

#获取九个点的坐标
google = {}
google[1] = (None,local["x"]+s["width"]/6,local["y"]+s["height"]/6)
google[2] = (None,local["x"]+s["width"]/6*3,local["y"]+s["height"]/6)
google[3] = (None,local["x"]+s["width"]/6*5,local["y"]+s["height"]/6)
google[4] = (None,local["x"]+s["width"]/6,local["y"]+s["height"]/6*3)
google[5] = (None,local["x"]+s["width"]/6*3,local["y"]+s["height"]/6*3)
google[6] = (None,local["x"]+s["width"]/6*5,local["y"]+s["height"]/6*3)
google[7] = (None,local["x"]+s["width"]/6,local["y"]+s["height"]/6*5)
google[8] = (None,local["x"]+s["width"]/6*3,local["y"]+s["height"]/6*5)
google[9] = (None,local["x"]+s["width"]/6*5,local["y"]+s["height"]/6*5)
print(google)

def pianyi(a=1,b=2):
    '''计算从a点到b点的偏移量'''
    g1 = google[a]
    g2 = google[b]
    r = (None, g2[1]-g1[1], g2[2]-g1[2])
    return r

#解锁思路：先press按住第一个点，再wait等待,接着移动带第二个点，再wait，最后release释放手指，perform执行
# 执行解锁
TouchAction(driver).press(*google[1]).wait(300).move_to(*pianyi(1,2)).wait(300).move_to(*pianyi(2,3)).wait(
    300).move_to(*pianyi(3,5)).wait(300).move_to(*pianyi(5,7)).wait(300).move_to(*pianyi(7,8)).wait(300).move_to(*pianyi(8,9)).wait(
    300).release().perform()