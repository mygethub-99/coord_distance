# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:49:47 2018
Creates a .txt file of distances between each psap and all sites sorted
@author: owen
"""
from geopy.distance import vincenty
from process_psap import makepsap as psap
from latlongwork import makesites as sites

getpsap = psap()
getsites = sites()

p = len(getpsap)
f = open("testfile.txt", "a+")
f.write("Distance between Psap and all sites")
f.write("\n")
mklist = []
if p > 0:
    for k in getpsap:
        psap_locate = getpsap[k]
        x = len(getsites)
        p = p-1
                
        while x > 0:
            temp = []
            for s in getsites:
                site_locate = getsites[s]
                dis = round(vincenty(psap_locate, site_locate).miles)
                x = x-1
                ut = (k, s, dis)
                temp.insert(0,ut)
                if x < 1:
                    sl = sorted(temp, key=lambda tup: (tup[2]))
                    mklist.insert(0,sl[0])
                
                #blank = list(map(int,swap_list))
                #swap_list=str(swap_list).strip('[]')
                #f.write(swap_list)
                #f.write("\n")
        
                    
    else:
        print (mklist)
        #list(map(int, mklist))
        #str(mklist).strip('[]')
        #f.write(mklist)
        #f.write("\n")
        
        with open('output.txt', 'w') as file_handler:
            for item in mklist:
                file_handler.write("{}\n".format(item))

        
        file_handler.close()
        f.close()


        
        
            
                
    
        
    
