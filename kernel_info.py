#!/usr/bin/python


from sysinfo_func import uname_func
import subprocess


def kernel_info():
    uname="uname"
    uname_opt="-r"
    print("Gathering kernel version using %s" % uname)
    subprocess.call([uname,uname_opt])


def main():
    uname_func()
    kernel_info()

if __name__=="__main__":
   uname_func()
   kernel_info()
