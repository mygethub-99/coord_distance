#Open a lat and long file of sites and place the sites in a
#Dictionary with the usid as the key and the lat and long as the value

def makesites():
    fopen = open('siteslatlong.txt')
    contents = fopen.readlines()
    fopen.close()
    sitedict = {}

#Using try and except to deal with "index exception" error caused by len function
#Except will subtract 1 from value of len(contents)     
    try:
        for line in range(1, len(contents)):
            line_split=contents[line].split()
            sitedict[line_split[0]]=line_split[1],line_split[2]
    except:
        for line in range(1, (len(contents))-1):
            line_split=contents[line].split()
            sitedict[line_split[0]]=line_split[1],line_split[2]
        
    return (sitedict)
makesites()
