import urllib2, google, bs4, re

def testwhen():
    q="when did the united states declare independence"
    r=google.search(q,num=10,start=0,stop=10)
    l=[]
    for result in r:
        l.append(result)

    #only opens first link
    url = urllib2.urlopen(l[0])
    page = url.read()
    soup = bs4.BeautifulSoup(page,'html')
    raw = soup.get_text()
    text = re.sub("[t\n ]"," ",raw)

    exp = "([0-9]{1,4}/[0-9]{1,4}/[0-9]{1,4})|([A-Z][a-z]+ [0-9]{0,2}, [0-9]{0,4})"

    result = re.findall(exp,text)

    return result

print testwhen()
