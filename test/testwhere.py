import urllib2, google, bs4, re

def testwhere():
    q="where does obama live"
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

    exp = "(T|t)he [A-Z][a-z]+ ?([A-Z][a-z]+ )+"

    result = re.findall(exp,text)

    return result

print testwhere()
