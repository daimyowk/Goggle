import urllib2, google, bs4, re
import utils

def findTime(query):
    file = open("words.txt")
    words = file.read()
    l = utils.search(query)
    goodDates=[]
    exp = """
    ([0-9]{1,4}/[0-9]{1,4}/[0-9]{1,4}) |
    ([A-Z][a-z]+ [0-9]{0,2}, [0-9]{1,4})
    """ 
        
    for pages in l:
        text = re.sub("[\t\n ]", " ", utils.get_page(pages))
        result = re.findall(exp, text)
        for x in result:
            goodDates.append(x)
    dateCount = {}
    for date in goodDates:
        if dateCount.has_key(date):
            dateCount[date]+=1
        else:
            dateCount[date]=1
    return dateCount

print findTime("When was the declaration of independence signed?")
