# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:45:27 2018
#example change 
@author: owen
"""
from geopy.distance import vincenty
getpsap = {1: ('32.458', '87.4220'), 2:('33.231', '87.3210')}
getsites= {1: ('34.458', '85.4220'), 2:('31.231', '83.3210')}
close_site = {}
sitekey=getsites.keys()
print (sitekey)
p=len(getpsap)
if p > 0:
    for value in getpsap.values():
        psap_locate=value
        x = len(getsites)
        p = p-1
        x = len(getsites)
        
        while x > 0:
            
            for value in getsites.values():
                site_locate=value
                all_distance=(vincenty(psap_locate, site_locate).miles)
                x = x-1
    else:
        print ("Thats all folks!")
                    
