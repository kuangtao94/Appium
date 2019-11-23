#封装工具类

import os
import xlrd
import logging

class Helper(object):
    def Readpath(self,filename='',filepath=''):
        '''定义存储数据的文件路径'''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)

    def ReadExcels(self,rows):
        '''读取excel文件xx行的数据'''
        book = xlrd.open_workbook(self.Readpath('Itestinfo.xlsx','Data'),'r')
        table = book.sheet_by_index(0)
        return table.row_values(rows)

    def log(self,log_content):
        '''日志定义级别'''
        # 定义文件
        logFile = logging.FileHandler(self.Readpath('logInfo.md','log'), 'a',encoding='utf-8')
        # log格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)

        # 定义日志
        logger1 = logging.Logger('logTest', level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)

    def Readusername(self,rows):
        '''读取文件中的用户数据'''
        return str(self.ReadExcels(rows)[0])

    def Readpassword(self,rows):
        '''读取文件中的密码数据'''
        return str(self.ReadExcels(rows)[1])

    def Readresult(self,rows):
        '''读取文件中的预期结果数据'''
        return self.ReadExcels(rows)[2]


# D:/Project/TestCase/App_Po\Data\Itestinfo.xlsx
per = Helper()
print(per.log('这是一个日志'))