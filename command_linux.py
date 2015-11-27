#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#Coded by Zirou
#NoSafe Rulez

import sys
import os

if len(sys.argv) <= 3:                # arv = ['./comando.py', 'ls', '-la']
    comando = ' '.join(sys.argv[1:])  # arv[1:] = ['ls', '-la']
    shell = os.system(comando)        # comando = 'ls -la'
    print comando
