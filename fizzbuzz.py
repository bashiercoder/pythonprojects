#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:49:41 2018

FizzBuzz Python Application

@author: bashier2026
"""

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)