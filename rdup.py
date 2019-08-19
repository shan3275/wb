#!/usr/bin/python
# coding:utf-8
#Filename:cup.py
# 用途：将日志自动上传到百度云盘中
# 1. 文件自动压缩
# 2. 当天将前一天的日志全部上传
# 3. 压缩日志上传之后，源文件及压缩文件自动删除
import time
import json
from collections import OrderedDict
import sys,os
import re
import base64
import requests
import tarfile
from optparse import OptionParser
import datetime
import subprocess
import hashlib,time,random, base64
import threading

global options
global method_rc4

def upload():
    ##获取当前的时间
    yesterday     =   datetime.date.today() - datetime.timedelta(days=1)
    yesterday_str =  yesterday.strftime('%Y-%m-%d')
    print yesterday_str
    real_file = '%s/result.log.%s' %(options.ipath, yesterday_str)
    print 'real_file:%s' %(real_file)
    rdup_file = '%s/rdup.log.%s' %(options.opath, yesterday_str)
    print 'rdup_file:%s' %(rdup_file)

    ##判断文件是否存在
    if os.path.exists(real_file) != True:
        return

    if os.path.exists(rdup_file) == True:
        return

    ## real_file 存在；去重文件不存在
    ##去重
    rdup_dict = {}
    rdup_count_dict = {}
    for line in open(real_file):
        array = line.split(';')
        #print(len(array))
        if len(array) < 6 :
            print('len of array is < 6')
            print(len(array))
            continue
        key = array[4]
        rdup_dict[key] = line
        if rdup_count_dict.has_key(key) :
            rdup_count_dict[key] = rdup_count_dict[key] + 1
        else :
            rdup_count_dict[key] = 1

    #写入文件
    f=open(rdup_file,'wb')

    for key, value in rdup_dict.items():
        print key,' count: ', rdup_count_dict[key], ' ', value
        f.writelines(value)

    #关闭文件
    f.close()

    return


    return






def fun_timer():
    upload()
    print time.strftime('%Y-%m-%d %H:%M:%S')
    #global timer
    #timer = threading.Timer(5, fun_timer)
    #timer.start()

if __name__ == '__main__':
    print '开始时间：'
    print time.strftime('%Y-%m-%d %H:%M:%S')
    ##输入参数
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-i", "--ipath", type="string", dest="ipath", help="read log from FILENAME")
    parser.add_option("-o", "--opath", type="string", dest="opath", help="output FILENAME")

    (options, args) = parser.parse_args()

    if options.ipath == None :
        parser.error("Invaild param")

    if options.opath == None :
        parser.error("Invaild param")

    timer = threading.Timer(5, fun_timer)
    timer.start()
