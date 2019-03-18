# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:49:47 2018
Creates a .txt file of distances between each psap and closes site
@author: owen
"""
from geopy.distance import geodesic
from process_psap import makepsap as psap
from latlongwork import makesites as sites

#Define the PSAP and Site variables that are dictionarys
getpsap = psap()
getsites = sites()

p = len(getpsap)
mklist = []

#For loop for iterating through each psap
if p > 0:
    for k in getpsap:
        psap_locate = getpsap[k]
        x = len(getsites)
        p = p-1
                
#Loop to create a temp list of psap with closes site in miles
        while x > 0:
            temp = []
            for s in getsites:
                site_locate = getsites[s]
                dis = round(geodesic(psap_locate, site_locate).miles, 2)
                x = x-1
                ut = (k, s, dis)
                temp.insert(0,ut)
                if x < 1:
                    sl = sorted(temp, key=lambda tup: (tup[2]))
                    mklist.insert(0,sl[0])

#Write mklist to a file in a coma seperated format                
    else:
        with open('PsaptoSiteSort.txt', 'w') as file_handler:
            file_handler.write("PSAPID, SiteID, Distance")
            file_handler.write("\n")
            for item in mklist:
                item = str(item).strip('()')
                item = item.replace("'", "")
                file_handler.write("{}\n".format(item))
        
        file_handler.close()
      


        
        
            
                
    
        
    
