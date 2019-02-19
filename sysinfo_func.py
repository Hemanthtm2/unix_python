#!/usr/bin/python
import subprocess
def uname_func():
    uname="uname"
    uname_arg="-a"
    print("Gathering system info using %s"% uname)
    subprocess.call([uname,uname_arg])
def disk_func():
    disk_sp="df"
    disk_arg="-h"
    print("Gathering disk info using %s"% disk_sp)
    subprocess.call([disk_sp,disk_arg])

def main():
    uname_func()
    disk_func()

if __name__=="__main__":
   main()
