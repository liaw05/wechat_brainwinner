# -*- coding: utf-8 -*-
"""
决胜“微信——头脑王者”
Created on Tue Jan 30 21:22:31 2018

@author: liaw05
"""
from resoures import screenshot, ocr, searchanswer, clickanswer
from PIL import Image

ready = 1
while ready:
    screenshot.pull_screenshot()
    ready = screenshot.check_screenshot()
   # print(ready)
#提前计算问题和答案区域
image = Image.open('./temp/screenshot.png')
region = ocr.cal_region(image)
#准备开始
ready = 1
while ready:
    ready = input("按ENTER开始, n 退出\n")
    if ready == 'n':
        break
    if not ready:
        ready = 1
        screenshot.pull_screenshot()
        image = Image.open('./temp/screenshot.png')
        question, answer = ocr.ocr_img(image, region)
        answerid = searchanswer.count_choices(question,answer)
        clickanswer.click(region, answerid)
        print(answer[answerid])
    
    

