#基础类的方法封装

class BasePage(object):
    #构造方法
    def __init__(self,driver):
        self.driver = driver

    #构造By_id 定位的改写
    def by_id(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as message:
            print('元素定位抛出异常，异常原因为:{}'.format(message))

    # 构造By_name 定位的改写
    def by_name(self, loc):
        try:
            return self.driver.find_element_by_name(loc)
        except Exception as message:
            print('元素定位抛出异常，异常原因为:{}'.format(message))

    # 构造By_xpath 定位的改写
    def by_xpath(self, loc):
        try:
            return self.driver.find_element_by_xpath(loc)
        except Exception as message:
            print('元素定位抛出异常，异常原因为:{}'.format(message))

    #构造By_classname 定位的改写
    def by_classname(self,loc):
        try:
            return self.driver.find_element_by_classname(loc)
        except Exception as message:
            print('元素定位抛出异常，异常原因为:{}'.format(message))