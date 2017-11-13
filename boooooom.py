#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '3.6'

import os
import sys
import rarfile
import zipfile
import argparse
import threadpool
from math import pow
from time import sleep
from brute import brute 
from datetime import datetime


def list_mix_up(a_list):
    pass

def add_zero_to_string(num, length):
    """
    int(1) to string list('1','01','001'...)
    """
    str_list = []
    for i in range(1, length-len(str(num))+1):
        str_list.append('0'*i + str(num))
    return str_list

def generator_pwd(mode):
    """
    return a generator
    """
    pwd_max_length = int(mode.split('_')[-1])
    print('generating password...')
    for i in range(int(pow(10, pwd_max_length))):
        pwd_list = []
        pwd_list.append(str(i))
        if len(str(i)) < pwd_max_length:
            i_list = add_zero_to_string(i, pwd_max_length)
            pwd_list.extend(i_list)
        yield pwd_list

def pwd_from_dict():
    pass


def cracker(file_name, file_type, mode=None):
    if file_type == 'zip':
        zip_file = zipfile.ZipFile(file_name, 'r')
    elif file_type == 'rar':
        rar_file = rarfile.RarFile(file_name, 'r')
    
    pwd_gen = generator_pwd(mode)
    times = 0
    start_time = datetime.now()
    for pwd_list in pwd_gen: # pwd_list = ['0','000'...]
        for pwd in pwd_list:
            times += 1
            sys.stdout.write('{} {}, '.format('try times:', times))
            sys.stdout.write('{} {}\r'.format('try password:', pwd))
            sys.stdout.flush()
            try:
                if file_type == 'zip':
                    zip_file.extractall(pwd=str.encode(pwd))
                elif file_type == 'rar':
                    rar_file.extractall(pwd=pwd)
                print("file extracted")
                print("!!!the password is %s" % pwd)
                print('tried times:', times)
                print('time consuming:', (datetime.now() - start_time).microseconds/1000/1000, 's')
                return True
            except:
                pass

    return False

    


def multi_thread():
    pass
    # pool = threadpool.ThreadPool(4)
    # t_requests = threadpool.makeRequests(save_video, urls)
    # [pool.putRequest(req) for req in t_requests]
    # pool.wait()

def cracker_main():
    """
    entrance function
    """
    parser = argparse.ArgumentParser(description='rar/zip Cracker')
    parser.add_argument('--file', help='file name')
    parser.add_argument('--mode', help='password generate mode')
    parser.add_argument('--process_num', help='process num')
    results = parser.parse_args()
    if not results.mode:
        print('No mode. Auto generate.')
    else:
        pass
    file_name = results.file
    if not os.path.isfile(file_name):
        print('Invilid file.')
        return 
    file_type = file_name.split('.')[-1]
    is_crack = cracker(file_name, file_type, results.mode)
    if not is_crack:
        print('sorry, please try another way.')

if __name__ == '__main__':
    cracker_main()
