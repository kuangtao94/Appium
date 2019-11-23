from appium import webdriver
from tomorrow import threads
import yaml
import os
import time as t

def start_appium(port = 4723,udid="4871660c"):
    a = os.popen("netstat -ano | findstr '%s'"%port)
    t.sleep(2)
    t1 = a.read()
    print(t1)
    if "LISTENING" in t1:
        print("appium服务已经启动%s"%t1)
        # s = t1.split(" ")
        # s1 = [t for t in s if t != " "]
        # pip = s1[-1].replace("\n","")
    else:
        # 启动appium服务
        # appium -a 127.0.0.1 -p 4740 -U emulator-5554 127.0.0.1:62001 --no-reset
        os.system("appium -a 127.0.0.1 -p %s -U %s --no-reset" % (port, udid))
        print("Error")

start_appium()


