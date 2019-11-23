import unittest
import os
import time
from HTMLTestRunner import HTMLTestRunner

def alltest():
    '''获取testcase下的所有测试模块'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__),'testcase'),
        pattern='Itest_login.py',
        top_level_dir=None
    )
    return suite

def getNowtime():
    '''获取当前的时间'''
    return time.strftime('%Y_%m_%d %H_%M_%S')

def run():
    '''主函数入口'''
    fp = open(os.path.join(os.path.dirname(__file__),'report',getNowtime() + 'report.html'),'wb')
    HTMLTestRunner(
        stream=fp,
        title='Appium自动化测试框架设计',
        description='基于python语言的appium自动化测试框架设计'
    ).run(alltest())

if __name__ == '__main__':
    run()

