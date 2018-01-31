# -*- coding: utf-8 -*-
"""
在百度网页上搜索并确定答案
Created on Tue Jan 30 19:15:58 2018

@author: Administrator
"""
import numpy
import requests

def count_choices(question,choices):
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text
    counts = []
    for i in range(len(choices)):
        counts.append(content.count(choices[i]))
        #print(choices[i] + " : " + str(counts[i]))
    counts = numpy.array(counts).argsort()
    #否定题,则选计数最少的
    if '不是' in question:
        return counts[0]
    else:
        return counts[-1]
    
if __name__ == '__main__':
    question = '张学友的经典国语歌 《秋意浓》 的粤语版叫什么名字?'
    choices = ['夜凋零', '菊花台', '不清楚', '李香兰']
    answerid = count_choices(question,choices)
    print(choices[answerid])