# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:49:47 2018
Creates a .txt file of distances between each psap and all sites
@author: owen
"""
from geopy.distance import vincenty
from process_psap import makepsap as psap
from latlongwork import makesites as sites

getpsap = psap()
getsites = sites()

swap_list = []
p = len(getpsap)
f = open("testfile.txt", "a+")
f.write("Distance between Psap and all sites")
f.write("\n")
if p > 0:
    for k in getpsap:
        psap_locate = getpsap[k]
        x = len(getsites)
        p=p-1
                
        while x > 0:
            for s in getsites:
                site_locate = getsites[s]
                dis=round(vincenty(psap_locate, site_locate).miles)
                x = x-1
                swap_list = (k, s, dis)
                swap_list = list(map(int,swap_list))
                swap_list=str(swap_list).strip('[]')
                f.write(swap_list)
                f.write("\n")
                    
    else:
        print ("Big Dictionary!")
        f.close()
        
        
            
                
    
        
    
