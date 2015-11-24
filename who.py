import urllib2, google, bs4, re
from stop_words import get_stop_words

def findPerson(query):
    file = open("words.txt")
    words = file.read()
    r = google.search("who played spiderman", num = 10, start = 0, stop = 10)
    l = []
    goodWords=[]
    exp = "[A-Z][a-z][a-z]+ [A-Z][a-z]+"

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
            z = x.split(" ")
            if z[0].lower() not in words and z[1].lower() not in words:
                goodWords.append(x)
    wordcounts={}
    for word in goodWords:
        if wordcounts.has_key(word):
            wordscounts.word+=1
        else:
            wordscounts[word]=1
    return wordscounts

print findPerson("Who played Spider Man?")
