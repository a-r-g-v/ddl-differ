#!/usr/bin/python3

import sys
import os
import sqlite3
import shutil
import time


def help():

    text = (
	'Usage:\n'
	' ddldiffer dump        Reverse MySQL Server and Dump DDL  \n'
        ' ddldiffer diff        Compare dump DDL to local file'
    )
    print(text)
    return

def dump():

    return

def diff():
    return 

if __name__ == "__main__":
    
    argvs = sys.argv
    if len(argvs) < 2:
        help()
    elif argvs[1] == "dump":
        dump()
    elif argvs[1] == "diff":
        diff()
    else:
        print("Undefined operand");

