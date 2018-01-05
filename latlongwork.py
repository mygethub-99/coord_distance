#Open a lat and long file of sites and place the sites in a
#Dictionary with the usid as the key and the lat and long as the value

def makesites():
    filename = 'siteslatlong.txt'
    fopen1 = open(filename, 'r')
    contents = fopen1.readlines()
    fopen1.close()
    

    sitedict={}

    for line in range(1, len(contents)):
        line_split=contents[line].split()
        #print (line_split)
        sitedict[line_split[0]]=line_split[1],line_split[2]

    return sitedict
makesites()
