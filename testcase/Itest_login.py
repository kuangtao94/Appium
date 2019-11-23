from TestCase.App_Po.common.Myunit import myunit
from TestCase.App_Po.common.function import *
from TestCase.App_Po.page.Page_login import PageItest
from TestCase.App_Po.Utils.helper import Helper
import unittest

#类的继承
class Itest_Login(PageItest,myunit,Helper):
    def test_Itest_success(self):
        '''验证登录成功:账号和密码输入正确'''
        self.log('logging日志信息:输入账号和密码')
        self.ITest.Itest_login_liucheng(self.Readusername(1),self.Readpassword(1))
        self.log('logging日志信息:对登录结果进行验证')
        self.assertEqual(self.ITest.login_success(), self.Readresult(1), '测试用例成功')
        self.log('logging日志信息:对登录成功进行截图')
        #实现截图功能 必须是png格式(官方指定)
        insert_image(self.driver,'success_info.png')

    def test_Itest_error2(self):
        '''验证登录失败:账号正确密码为空'''
        self.log('logging日志信息:输入账号和密码为空')
        self.ITest.Itest_login_liucheng(self.Readusername(2),self.Readpassword(2))
        self.log('logging日志信息:对登录结果进行验证')
        self.assertEqual(self.ITest.login_error(),  self.Readresult(2), '测试用例失败')
        self.log('logging日志信息:对登录失败进行截图')
        # 实现截图功能 必须是png格式(官方指定)
        insert_image(self.driver, 'passwd_null.png')

    def test_Itest_error3(self):
        '''验证登录失败:账号为空密码正确'''
        self.log('logging日志信息:输入账号为空和密码正确')
        self.ITest.Itest_login_liucheng(self.Readusername(3),self.Readpassword(3))
        self.log('logging日志信息:对登录结果进行验证')
        self.assertEqual(self.ITest.login_error(), self.Readresult(3), '测试用例失败')
        self.log('logging日志信息:对登录失败进行截图')
        # 实现截图功能 必须是png格式(官方指定)
        insert_image(self.driver, 'username_null.png')

    def test_Itest_error4(self):
        '''验证登录失败:账号非法密码正确'''
        self.log('logging日志信息:输入账号非法和密码正确')
        self.ITest.Itest_login_liucheng(self.Readusername(4),self.Readpassword(4))
        self.log('logging日志信息:对登录结果进行验证')
        self.assertEqual(self.ITest.login_error(), self.Readresult(4), '测试用例失败')
        self.log('logging日志信息:对登录失败进行截图')
        # 实现截图功能 必须是png格式(官方指定)
        insert_image(self.driver, 'username_Fail.png')

    def test_Itest_error5(self):
        '''验证登录失败:账号为空密码为空'''
        self.log('logging日志信息:输入账号和密码都为空')
        self.ITest.Itest_login_liucheng(self.Readusername(5),self.Readpassword(5))
        self.log('logging日志信息:对登录结果进行验证')
        self.assertEqual(self.ITest.login_error(), self.Readresult(5), '测试用例失败')
        self.log('logging日志信息:对登录失败进行截图')
        # 实现截图功能 必须是png格式(官方指定)
        insert_image(self.driver, 'username_passwd_null.png')

if __name__ == '__main__':
    unittest.main(verbosity=2)


