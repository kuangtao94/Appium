#移动Web应用App测试
#在pc端定位元素

from appium import webdriver
from time import sleep

desired_caps = {
        'deviceName':'Android Emulator',
        'automationName':'Appium',
        'platformName':'Android',
        'platformVersion':'7.0',
        'browserName':'Chrome',
        'noReset':True
}

driver = webdriver.Remote('http://localhost:4732/wd/hub',desired_caps)

driver.get('http://m.baidu.com')

driver.find_element_by_id('index-kw').send_keys('appium mobile web')
driver.find_element_by_id('index-bn').click()
sleep(5)

driver.quit()