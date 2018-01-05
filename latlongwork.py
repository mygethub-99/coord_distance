#Open a lat and long file of sites and place the sites in a
#Dictionary with the usid as the key and the lat and long as the value
from geopy.distance import vincenty

#Open file of cell site locations
filename = 'siteslatlong.txt'
fopen1 = open(filename, 'r')
contents = fopen1.readlines()

#Open file of PSAP locations
filename2 = 'psap_list.txt'
fopen2 = open(filename2, 'r')
cont2 = fopen2.readline()


for line in range(1, len(cont2)):
    splitsit=cont2[line].split()
    print (splitsit)
                   
                  


sitedict={}

for line in range(1, len(contents)):
    line_split=contents[line].split()
    #print (line_split)
    sitedict[line_split[0]]=line_split[1],line_split[2]
