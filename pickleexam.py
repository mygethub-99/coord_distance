# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle


output = open('output.txt', 'ab+')
data = {'a': [1, 2, 3],}

pickle.dump(data, output)
output.close()

# read data
output = open('output.txt', 'rb')
obj_dict = pickle.load(output)  
