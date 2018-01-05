#Create the psap dictionary with usid as key


def makepsap():
    filename2 = 'psap_list.txt'
    fopen2 = open(filename2, 'r')
    cont2 = fopen2.readlines()
    psap_dict = {}
    fopen2.close()

    for line in range(1, len(cont2)):
        splitsit=cont2[line].split()
        psap_dict[splitsit[0]]=splitsit[1],splitsit[2]
    
    return (psap_dict)

makepsap()
