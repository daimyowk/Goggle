import urllib2, google, bs4, re
from stop_words import get_stop_words

def test():
    file = open("../words.txt")
    words = file.read()

    q="who played spiderman"
    r = google.search(q,num=1,start=0,stop=1)
    l=[]
    for result in r:
        l.append(result)

    
    u = urllib2.urlopen(l[0])
    page = u.read()
    soup = bs4.BeautifulSoup(page,'html')
    raw = soup.get_text()
    text = re.sub("[\t\n ]"," ",raw)
    
    exp = "[A-Z][a-z][a-z]+ [A-Z][a-z]+"
    result = re.findall(exp,text);
    goodWords=[]

    for x in result:
        z = x.split(" ")
        if z[0].lower() not in words and z[1].lower() not in words:
                goodWords.append(x)
    return goodWords

def test2():
    stop_words = get_stop_words('en')
    return stop_words

print test()


