#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '3.6'

import zipfile
import os
import sys
from unrar import rarfile
from brute import brute 
from datetime import datetime

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

def cracker_rar(file_name):
    file_name = '33333.rar'
    rar_file = rarfile.RarFile(file_name, 'r')
    print('read over.')
    pwd_list = generater_pwd(mode='number,3')
    times = 0
    for pwd in pwd_list:
        times += 1
        print('try times:', times)
        try:
            print(pwd)
            rar_file.extractall(pwd=str.encode(pwd))
            print("file extracted")
            print("the password is %s" % pwd)
            break
        except:
            print('pass')
            pass
    rar_file.close()

def cracker_zip(file_name):
    file_name = 'rules.zip'
    zip_file = zipfile.ZipFile(file_name, 'r')
    pwd_list = generater_pwd(mode='number,3')
    times = 0
    start_time = datetime.now()
    for pwd in pwd_list:
        times += 1
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

def cracker():
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        print('Invilid file.')
        return 
    file_type = file_name.split('.')[-1]
    if file_type == 'zip':
        cracker_zip(file_name)
    if file_type == 'rar':
        cracker_rar(file_name)

if __name__ == '__main__':
    cracker()