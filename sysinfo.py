#!/usr/bin/python

import subprocess 

uname="uname"
uname_arg="-a"

print("Gathering system information using command %s\n"% uname)

subprocess.call([uname,uname_arg])
print("\n")
diskspace="df"
disk_arg="-h"
print("Gathering disk space information using command %s\n" % diskspace)

subprocess.call([diskspace,disk_arg])
