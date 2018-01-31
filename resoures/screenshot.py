# -*- coding: utf-8 -*-
"""
手机屏幕截图的代码
"""

import os
from PIL import Image

def pull_screenshot():
    """
    获取手机屏幕截图
    """
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png ./temp/')
    
def check_screenshot():
    """
    检查截屏是否正常
    """
    try:
        Image.open('./temp/screenshot.png')
        return 0
    except Exception:
        print('请检查连接是否正确')
        return 1

if __name__ == '__main__':
    pull_screenshot()
    check_screenshot()