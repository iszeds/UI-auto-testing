#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import random
import string

class MyClass(object):
    def __init__(self):
        pass
 
# kill chromedriver
    def Kill_Chromedriver(self):
        os.system("taskkill /f /im chromedriver.exe")
# random 
    def Random_char_by_length(self, result_type, length):
        length = int(length)
        result = []
        if result_type == 'Number':
            for i in range(length):
                rand = random.randint(0,9)
                result.append(str(rand))
            result = int(''.join(result))
            #print (result)
            return result
    def Random_char_by_scope(self, result_type, min, max):
        min = int(min)
        max = int(max)
        if result_type == 'Number':
            result = random.randint(min,max)
            print (result)
            return result




# Test
if __name__ == '__main__':
    MyClass().Kill_Chromedriver()

