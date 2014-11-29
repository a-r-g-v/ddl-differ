#!/usr/bin/python3

import sys
import os
import os.path
import shutil
import time
import configparser


def init():
    global config
    config = configparser.SafeConfigParser()
    config.read("ddldiffer.conf")
    path = config.get('local','sqlpath');
    if os.path.exists(path) != True:
        print("Can't accesss sqlpath :", path);
        exit(-1)
    return config

def help():
    text = (
	'Usage:\n'
	' ddldiffer dump        Reverse MySQL Server and Dump DDL  \n'
        ' ddldiffer diff        Compare dump DDL to local file'
    )
    print(text)
    return

def readConfig(section,key):
    result = config.get(section, key)
    # TODO Error Check
    return result

def dump():
    # Ready Connect Database
    host = readConfig('database','host')
    user = readConfig('database','user')
    passwd = readConfig('database','passwd')
    port = readConfig('database', 'port')
    db = readConfig('database','database')

    # Connect


    # GetTableList


    # GetDDL


    # DisConnect

    return

def diff():
    return 

if __name__ == "__main__":
    init()    
    argvs = sys.argv
    if len(argvs) < 2:
        help()
    elif argvs[1] == "dump":
        dump()
    elif argvs[1] == "diff":
        diff()
    else:
        print("Undefined operand");


