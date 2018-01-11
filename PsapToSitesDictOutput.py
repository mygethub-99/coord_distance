# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:49:47 2018
Creates a nested Dictionary of distances between each psap and all sites
@author: owen
"""
from geopy.distance import vincenty
from process_psap import makepsap as psap
from latlongwork import makesites as sites
import operator

getpsap = psap()
getsites = sites()
psap_dict = {}
swap_list = []
p = len(getpsap)
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
                swap_list = [k, s, dis]
                try:
                    psap_dict[swap_list[0]][swap_list[1]] = {'Distance':swap_list[2]}
                except:
                    psap_dict[swap_list[0]] = {}
                    psap_dict[swap_list[0]][swap_list[1]] = {'Distance':swap_list[2]}
                    
               
                    
                s
                
    else:
        print ("Big Dictionary!")
        
            
                
    
        
    
