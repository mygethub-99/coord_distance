#Create the psap dictionary with usid as key


def makepsap():
    fopen2 = open('psap_list.txt')
    cont2 = fopen2.readlines()
    psap_dict = {}
    fopen2.close()
    
    try:
        for line in range(1, len(cont2)):
            splitsit=cont2[line].split()
            psap_dict[splitsit[0]]=splitsit[1],splitsit[2]
    
    except:
        for line in range(1, (len(cont2))-1):
            splitsit=cont2[line].split()
            psap_dict[splitsit[0]]=splitsit[1],splitsit[2]
    
    return (psap_dict)
    

makepsap()
