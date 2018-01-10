# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:45:27 2018
#example change 
@author: owen
"""
import operator
from geopy.distance import vincenty
getpsap = {1: ('32.458', '87.4220'), 2:('33.231', '87.3210')}
getsites= {1: ('34.458', '85.4220'), 2:('31.231', '83.3210')}
site_keys = list(getsites.keys())
print (site_keys)

list1 = [1, 2, 3, 4, 5]
list2 = [123, 234, 456]
d = {'a': [], 'b': []}
d['a'].append(list1)
d['a'].append(list2)
print (d['a'])
print (d)
play_diction = {1: ('32.458', '87.4220'),('30',  2:('33.231', '87.3210')}

