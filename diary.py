#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:05:41 2021

@author: EduardoWork
"""

import datetime

with open('my_diary.txt', 'a') as fp:

    while True:

        entry = input('What are you doing now? (Type quit to exit) ')

        if entry.lower() == 'quit':
            break

        date = datetime.datetime.now()
        date = date.strftime('%d/%m/%Y %H:%M')

        fp.write(f'\n{date} - {entry}')
