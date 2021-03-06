#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:24:20 2021

@author: EduardoWork
"""

with open('book.txt', 'r') as file:

    character = 'Tom'
    count = 0

    for line in file:
        count += line.count(character)

    print(f'\nThe character {character} shows up {count} times.')
