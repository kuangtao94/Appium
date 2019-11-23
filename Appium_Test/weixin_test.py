from appium import webdriver
from time import sleep

desired_caps = {
    "platformName":"Android",
    "platformVersion":"9",
    "deviceName":"4871660c",
    "appPackage":"com.tencent.mm",
    "appActivity":".ui.LauncherUI",
    "chromeOptions":"{'androidProcess':'com.tencent.mm:tools'}",
    "automationName":"Uiautomator2",
    "unicodeKeyboard":True,
    "resetKeyboard":True,
    "noReset":True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)

try:
    #点微信首页搜索按钮
    driver.find_element_by_id("com.tencent.mm:id/jb").click()

    #输入内容搜索
    sleep(3)
    id_text = 'resourceId("com.tencent.mm:id/l3").text("搜索")'
    driver.find_element_by_android_uiautomator(id_text).send_keys("yoyoketang\n")

    #点开公众号
    sleep(3)
    id_text1 = 'resourceId("com.tencent.mm:id/qm").text("从零开始学自动化测试")'
    driver.find_element_by_android_uiautomator(id_text1).click()

    #点击公众号菜单-2019课程
    # sleep(3)
    # id_text2 = 'resourceId("com.tencent.mm:id/an0").text("2019课程")'
    # driver.find_element_by_android_uiautomator(id_text2).click()
    # contexts = driver.contexts
    # print(contexts)

    #切换webview
    # sleep(3)
    # driver.switch_to_default_content("WEBVIEW_com.tencent.mm:tools")

    #点击用户名-- 上海
    # sleep(3)
    # id_text3 = 'resourceId("js_author_name").text("上海悠悠")'
    # driver.find_element_by_android_uiautomator(id_text3).click()
    # print(driver.contexts)

    #点击历史记录 -- django教程
    sleep(3)
    id_text4 = 'resourceId("com.tencent.mm:id/an0").text("历史记录")'
    list1 = driver.find_element_by_android_uiautomator(id_text4).click()
    # list1 = driver.find_elements_by_xpath("//*[@text='历史记录']").click()
    print(type(list1),list1)
    print(driver.contexts)
    # driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    # class_text = 'className("android.widget.TextView").text("django教程")'
    # driver.find_element_by_android_uiautomator(class_text).click()
    # contexts = driver.contexts
    # print(contexts)

    # sleep(3)
    # driver.switch_to.context( 'NATIVE_APP')
    #

    #
    #点击django合集
    # id_text5 = 'resourceId("com.tencent.mm:id/cx").text("django合集")'
    # driver.find_element_by_android_uiautomator(id_text5).click()
    # print(driver.contexts)


    # id_text6 = 'resourceId("activity-name").text("django合集")'
    # apps = driver.find_elements_by_android_uiautomator(id_text6)
    # for item in apps:
    #     print(item)

except Exception :
    print("Error")
    #退出微信应用
    driver.quit()

