#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '3.6'

import argparse
import zipfile
import os
import sys
import rarfile
from time import sleep
from brute import brute 
from datetime import datetime
from progressive.bar import Bar


def generater_pwd(mode):
    # length = int(mode.split(',')[1])
    # while length > 1:
    #     length -= 1
    pwd_list = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    pwd = str(i)+str(j)+str(k)+str(l)
                    pwd_list.append(pwd)
    print('length:', len(pwd_list))
    return pwd_list

def pwd_from_dict():
    pass

def cracker_rar(file_name, mode=None):
    rar_file = rarfile.RarFile(file_name, 'r')
    pwd_list = generater_pwd(mode='number,3')
    times = 0
    for pwd in pwd_list:
        times += 1
        print('try times:', times)
        try:
            print('try password:',pwd)
            rar_file.extractall(pwd=pwd)
            print("file extracted")
            print("the password is %s" % pwd)
            break
        except:
            pass
    rar_file.close()

def cracker_zip(file_name, mode=None):
    zip_file = zipfile.ZipFile(file_name, 'r')
    pwd_list = generater_pwd(mode='number,3')
    times = 0
    start_time = datetime.now()

    bar = Bar(max_value=len(pwd_list))
    bar.cursor.clear_lines(2)  # Make some room
    bar.cursor.save()  # Mark starting line
    # for i in range(101):
        # sleep(0.1)  # Do some work
        # bar.cursor.restore()  # Return cursor to start
        # bar.draw(value=i)  # Draw the bar!

    for pwd in pwd_list:
        times += 1
        sleep(0.1)  # Do some work
        bar.cursor.restore()  # Return cursor to start
        bar.draw(value=times)  # Draw the bar!


        print('try times:', times)
        try:
            print(pwd)
            zip_file.extractall(pwd=str.encode(pwd))
            print("file extracted")
            print("the password is %s" % pwd)
            break
        except:
            pass
    zip_file.close()
    print('tried times:', times)
    print('time consuming:', (datetime.now() - start_time).microseconds/1000/1000, 's')

def cracker_main():


    parser = argparse.ArgumentParser(description='rar/zip Cracker')
    parser.add_argument('--file', help='file name')
    parser.add_argument('--mode', help='password mode')
    results = parser.parse_args()
    if not results.mode:
        print('No mode. Auto generate.')
    else:
        pass

    # file_name = sys.argv[1]
    file_name = results.file
    if not os.path.isfile(file_name):
        print('Invilid file.')
        return 
    file_type = file_name.split('.')[-1]
    if file_type == 'zip':
        cracker_zip(file_name)
    if file_type == 'rar':
        cracker_rar(file_name)

if __name__ == '__main__':
    cracker_main()