#!/usr/bin/python
# -*- coding:utf-8 -*-
#14th Aug  2017 Emacs_yang

import os
import time
import requests
from threading import Thread

path = "/home/heyang/mywork/mydoc/"

def postfile(arg):

    if os.path.isfile(os.path.join(path,str(arg)+".doc")) == True:
        #post_data = {'shalfile':'abc'}
        print "begin doc %d time %s" % (arg,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        post_file = {'myfile':open(path+str(arg)+".doc", 'rb')}

    elif os.path.isfile(os.path.join(path,str(arg)+".docx")) == True:
        print "begin docx %d time %s" % (arg,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        post_file = {'myfile':open(path+str(arg)+".docx", 'rb')}
    else:
        print "document file%d error" % arg
        return
    r= requests.post("http://192.168.0.196:8000/testuploadfile",files=post_file)
    time.sleep(1)
    print r
    print "%d.docx end time %s" % (arg, time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

def multithreading():
    threads = []
    count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))])
    for i in range(count):
        t = Thread(target=postfile,args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def debugInfo(filename,status):
    return "%s %s time %s" % (suffix,status, time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

if __name__ == "__main__":
    multithreading()
