#原生应用app测试

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
        'deviceName':'Android Emulator',
        'automationName':'Appium',
        'platformName':'Android',
        'platformVersion':'7.0',
        'appPackage':'com.android.contacts',
        'appActivity':'.activities.PeopleActivity',
        'noReset':True
}

driver = webdriver.Remote('http://localhost:4732/wd/hub',desired_caps)

#单击添加按钮
TouchAction(driver).tap(945,1425).perform()

#输入联系人信息
driver.find_element_by_android_uiautomator('text("Name")').send_keys('Omy')
driver.find_element_by_android_uiautomator('text("Phone")').send_keys('124525151')

#保存联系人
driver.find_element_by_id('com.android.contacts:id/menu_save').click()

driver.quit()