# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:47:12 2018

@author: owen
"""
#Created to play with map function.

T1 = (('13', '17', '18', '21', '32'),
      ('07', '11', '13', '14', '28'),
      ('01', '05', '06', '08', '15', '16'))

T2 = [list(map(int, x)) for x in T1]
#print (T2)
swap_list = ('8', '42234', '13')

             
a = ['1', '2', '3']
a = list(map(int,a))
print (a)
