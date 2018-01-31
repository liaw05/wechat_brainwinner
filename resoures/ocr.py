# -*- coding: utf-8 -*-
"""
根据比例裁剪问题区和答案区
用tesseract_ocr 识别中文字符
Created on Tue Jan 30 12:25:37 2018

@author: Administrator
"""

import pytesseract
from PIL import Image

# 二值化算法
def binarizing(img, threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

#计算区域坐标
def cal_region(image):
    w, h = image.size
    #根据比例裁剪问题区域
    question_region = (int(0.123*w), int(0.28*h), int(0.873*w), int(0.428*h))
    #根据比例裁剪答案区域
    answer_a_region = (int(0.233*w), int(0.439*h), int(0.771*w), int(0.514*h))
    answer_b_region = (int(0.233*w), int(0.539*h), int(0.771*w), int(0.614*h))
    answer_c_region = (int(0.233*w), int(0.639*h), int(0.771*w), int(0.714*h))
    answer_d_region = (int(0.233*w), int(0.739*h), int(0.771*w), int(0.814*h))
    region=[question_region, answer_a_region, answer_b_region, answer_c_region, answer_d_region]
    #print(region)
    return region

#识别图片文字
def ocr_img(image, region):
    text = []
    for i in range(len(region)):
        dregion = image.crop(region[i])
        dregion_b = binarizing(dregion.convert('L'), 190)
       # dregion_b.show()
        tt = pytesseract.image_to_string(dregion_b, lang='chi_sim')
        tt = tt.replace("\n", "")
        if tt:
            text.append(tt)
        else:
            text.append('不清楚!')
    question = text[0]
    answer = text[1:]
    return question, answer

#将答案区整体识别，已提高识别速度
def ocr_img_all(image, region):
    question_region = image.crop(region[0])
    question_region = binarizing(question_region.convert('L'), 190)
    question = pytesseract.image_to_string(question_region, lang='chi_sim')
    
    answer_region = image.crop((region[1][0], region[1][1], region[-1][2], region[-1][3]))
    answer_region = binarizing(answer_region.convert('L'), 190)
    #answer_region.show()
    answer_tt = pytesseract.image_to_string(answer_region, lang='chi_sim')
    answer_tt  = answer_tt .split('\n')
    answer = [x for x in answer_tt if x != '']
    return question, answer

if __name__ == '__main__':
    image = Image.open('./temp/screenshot.png')
    region = cal_region(image)
    question, answer = ocr_img_all(image, region)
    print(question)
    print(answer)