#!/usr/bin/python
'''
Simple program in python for stop services
specific

Coded by Zirou
GitHub => github.com/zirou30
'''

import os

s = ["apache2", "bluetooth", "mysql", "postgresql"]

for i in s:
    os.system("sudo service %s stop" %i)
