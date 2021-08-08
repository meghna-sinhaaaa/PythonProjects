#!/usr/bin/env python3
import os
import sys
import subprocess

# name = input("Please enter your name: ")
# print("Hello " + name)

# print("HOME" + os.environ.get("HOME",""))
# print("SHELL" + os.environ.get("SHELL",""))
# print("FRUIT" + os.environ.get("FRUIT",""))

#export FRUIT=Pineappple will add this is environment variable in linux

#print(sys.argv)

# filename = sys.argv[1]

# if not os.path.exists(filename):
    # with open(filename,"w") as f:
        # f.write("New file created\n")
# else:
    # print("Error, the {} file already exists.".format(filename))
    # sys.exit(1)
    
# value = subprocess.check_output(['ping','127.0.0.1'])
# print(value)

#ADVANCED SUBPROCESS MANAGEMENT

#bytes to string using decode() method
dictio = os.environ.copy()
print(dictio)


#PROCESSING LOG FILES

