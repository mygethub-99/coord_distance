from geopy.distance import vincenty
from process_psap import makepsap as psap
from latlongwork import makesites as sites



def makeit():
    getsites = sites()
    getpsap = psap()
    

    psapkeys = getpsap.keys()
    print (psapkeys)
    print (psapkeys[0])




makeit()
