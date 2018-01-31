# -*- coding: utf-8 -*-
"""
在手机屏幕上点击选择答案
Created on Tue Jan 30 20:35:14 2018

@author: Administrator
"""
import os

def click(region, answerid):
    x = int((region[answerid+1][0]+ region[answerid+1][2])/2)
    y = int((region[answerid+1][1]+ region[answerid+1][3])/2)
    cmd = 'adb shell input tap ' + str(x) + ' ' + str(y)
    #print(cmd)
    os.system(cmd)

    
if __name__ == '__main__':
    region = [(132, 537, 942, 821), (251, 842, 832, 986),\
              (251, 1034, 832, 1178), (251, 1226, 832, 1370), \
              (251, 1418, 832, 1562)]
    answerid = 2
    click(region, answerid)
