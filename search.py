# -*- coding:utf-8 -*-#

# filename: prt_cmd_color.py

import ctypes, sys
text=''
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 字体颜色定义 text colors
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_YELLOW = 0x0e  # yellow.

# 背景颜色定义 background colors
BACKGROUND_YELLOW = 0xe0  # yellow.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


# green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess + '\n')
    resetColor()


# red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess + '\n')
    resetColor()


# yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess + '\n')
    resetColor()


# white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess + '\n')
    resetColor()

def requesting(url):

    r = requests.get(url)
    if r.status_code == 200:
        printGreen("found: "+url+'  200[ok]')

    elif r.status_code == 500:
        printYellow("not sure: " + url +'   500')


def requesting_thread(url,mulu):
    print("tring "+url+mulu)
    r = requests.get(url+mulu)

    if r.status_code == 200:
        printGreen("found: "+url+'  200[ok]')

    elif r.status_code == 500:
        printYellow("not sure: " + url +'   500')





import requests
import time
import argparse
from multiprocessing.pool import ThreadPool
import time


parser = argparse.ArgumentParser(description='penson自研目录扫描器')
parser.add_argument('-u', type=str, help='传入url')
parser.add_argument('-t', type=int, help='自定义线程数',default=10)
parser.add_argument('-d', type=str, help='字典',default='1.txt')

args = parser.parse_args()


url = args.u
thread_number = args.t
directory = args.d



if thread_number ==0:
    printRed("当前线程数为0！！！！")
    with open(directory, 'r') as f:
        mulus = f.readlines()
        for mulu in mulus:
            re_mulu = mulu.replace('\n','')
            new_url = url+re_mulu
            print("tring "+new_url)
            requesting(new_url)
else:
    printRed(f"当前线程数为{thread_number}！！！")
    time.sleep(1)
    pool = ThreadPool(thread_number)
    with open(directory, 'r') as f:
        mulus = f.readlines()
        for mulu in mulus:
            re_mulu = mulu.replace('\n','')
            pool.apply_async(requesting_thread,args=(url,re_mulu,))


        pool.close()
        pool.join()



