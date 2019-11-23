# from selenium import webdriver
# import unittest_1, time


# class YoudaoTest(unittest_1.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
#         self.base_url = "http://www.youdao.com"
#
#     def test_youdao(self):
#         driver = self.driver
#         driver.get(self.base_url + "/")
#         driver.find_element_by_id("translateContent").clear()
#         driver.find_element_by_id("translateContent").send_keys(u"你好")
#         driver.find_element_by_id("translateContent").submit()
#         time.sleep(3)
#         page_source = driver.page_source
#         self.assertIn("hello", page_source)
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest_1.main()


from selenium import webdriver
import unittest_1, time


class BaiduTest(unittest_1.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("你好")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        print(title)
        self.assertEqual(title, "你好_百度搜索")
        url = driver.current_url
        print(url)
        self.assertIn("https://www.baidu.com/",url)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest_1.main(verbosity=2)