#!/usr/bin/python

from sysinfo_func import disk_func
import subprocess

def tmp_space():
    tmp="du"
    tmp_arg="-h"
    dir_name="/tmp"
    print("Disk consumption under %s" % dir_name)
    subprocess.call([tmp,tmp_arg,dir_name])

def main():
    disk_func()
    tmp_space()


if __name__=="__main__":

   main()
