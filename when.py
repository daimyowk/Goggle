import urllib2, google, bs4, re

def findTime(query):
    file = open("words.txt")
    words = file.read()
    r = google.search(query, num = 3, start = 0, stop = 3)
    l = []
    goodDates=[]
    exp = """
    ([0-9]{1,4}/[0-9]{1,4}/[0-9]{1,4}) |
    ([A-Z][a-z]+ [0-9]{0,2}, [0-9]{1,4})
    """

    for result in r:
        l.append(result)  
        
    for pages in l:
        u = urllib2.urlopen(pages)
        page = u.read()
        soup = bs4.BeautifulSoup(page, 'html')
        raw = soup.get_text()
        text = re.sub("[\t\n ]", " ", raw)
        result = re.findall(exp, text)
        for x in result:
            goodDates.append(x)
    dateCount={}
    for date in goodDates:
        if dateCount.has_key(date):
            dateCount[date]+=1
        else:
            dateCount[date]=1
    return dateCount

print findTime("When was the declaration of independence signed?")
