from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
descred_caps = {
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.baidu.yuedu",
    "appActivity":"com.baidu.yuedu.splash.SplashActivity",
    "automationName":"uiautomator2",
    "noRset":"true",
    "unicodeKeyboard":"true",
    "resetKeyboard":"true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",descred_caps)

#获取当前的avtivity
print(driver.current_activity)

#弹出个性化定制 -- 点击热门图书
# 等主页面activity出现
driver.wait_activity(".usercenter.view.activity.UserInterestSetActivity",10)
driver.wait_activity(".splash.SplashActivity",20)
# sleep(20)
try:
    #-- 点击文学艺术
    driver.find_element_by_id("com.baidu.yuedu:id/check_box_6").click()

    #男生爱读
    sleep(5)
    driver.tap([(132,833),(288,868)],500)
    sleep(4)
    driver.tap([(500,833),(657,868)],500)

    #点击选好了
    driver.find_element_by_id("com.baidu.yuedu:id/tv_next").click()

    #点击简约白
    driver.find_element_by_id("com.baidu.yuedu:id/rbtn_theme_white").click()
    driver.find_element_by_id("com.baidu.yuedu:id/cb_choose_view").click()
    #点击立即开启
    driver.find_element_by_id("com.baidu.yuedu:id/tv_open").click()

    #点击知道了
    driver.find_element_by_id("com.baidu.yuedu:id/positive").click()

    # 获取当前的avtivity
    print(driver.current_activity)
    print(driver.contexts)

    driver.back() #点返回
    # 定位toast元素
    toast_loc = ("xpath", ".//*[contains(@text,'再按一次退出')]")
    t = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
    print(t)

    #点击图书
    driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").click()

    # 获取text
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").text)

    #获取tag_name
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").tag_name)

    # content-desc为空，获取的是text
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").get_attribute("name"))

    #text
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").get_attribute("text"))

    #bounds
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").get_attribute("bounds"))

    #size
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").size)

    #location
    print(driver.find_element_by_id("com.baidu.yuedu:id/tv_tab_title").location)

except Exception:
    print("出错啦")
    # driver.quit()
