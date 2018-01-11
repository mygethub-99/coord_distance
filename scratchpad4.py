# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:49:47 2018

@author: owen
"""
from geopy.distance import vincenty
getpsap = {1: ('32.458', '87.4220'), 2:('33.231', '87.3210')}
getsites= {1: ('34.458', '85.4220'), 2:('31.231', '83.3210')}
psap_dict = {}
p = len(getpsap)
if p > 0:
    for k in getpsap:
        psap_locate = getpsap[k]
        x = len(getsites)
                
        while x > 0:
            for s in getsites:
                site_locate = getsites[s]
                dis=round(vincenty(psap_locate, site_locate).miles)
                x = x-1
                sl = (k,s,dis)
                if not psap_dict:
                    psap_dict[sl[0]] = {'Site':sl[1], 'Distance':sl[2]}
                else:
                    tempdict = {sl[]}
                    
                
                
    else:
        print (psap_dist)
            
                
    
        
    
