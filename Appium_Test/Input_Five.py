import os
import time as t

adb = 'adb shell input tap 400 500'
os.system(adb)

t.sleep(5)

class keyevent():
    """常用的keyevent事件"""
    KEYCODE_HOME = 3  #home键
    KEYCODE_BACK = 4  #back键
    KEYCODE_POWER = 26  #电源键
    KEYCODE_MENU = 82  #主菜单键
    KEYCODE_NOTIFICATION = 83  #锁屏键
    KEYCODE_DPAD_UP = 19  #向上
    KEYCODE_DPAD_DOWN = 20  #向下
    KEYCODE_DPAD_LEFT = 21  #向左
    KEYCODE_DPAD_RIGHT = 22  #向右

def adbkeyevent(keyname = keyevent.KEYCODE_BACK):
    """执行adb keyevent事件，参数从keyevent类里面关联"""
    adb1 = 'adb shell input keyevent %s'%keyname
    os.system(adb1)

if __name__ == '__main__':
    #执行back键操作
    adbkeyevent(keyevent.KEYCODE_BACK)


#注意：中文是没法输入的，比如：上海

adb2 = 'adb shell input text 1234'
os.system(adb2)

