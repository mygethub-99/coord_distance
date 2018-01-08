from geopy.distance import vincenty
from process_psap import makepsap as psap
from latlongwork import makesites as sites



def makeit():
    getsites = sites()
    getpsap = psap()
    x = 1
    
    while x > 0:
        for value in getpsap.values():
            psap_locate=value
            print (psap_locate)
        
            for value in getsites.values():
                site_locate=value
                all_distance=(vincenty(psap_locate, site_locate).miles)
                x = x-1
                #print (all_distance)
        
    psapkeys = getpsap.keys()
    for v in getpsap.values():
        geocode = ['33.456', '87.3432']
        #x = (vincenty(jack, geocode).miles)
        #print (x)




makeit()
