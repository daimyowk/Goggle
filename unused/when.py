import urllib2, google, bs4, re
from stop_words import get_stop_words
import utils

def findPerson(query):
    """
    returns the name that shows up the most from the google search of the query

    arguments:
      string of the question

    return:
      name of a person
    """   
    file = open("words.txt")
    words = file.read()
    l = utils.search(query)
    goodWords=[]
    exp = "[A-Z][a-z][a-z]+ [A-Z][a-z]+"  
        
    for pages in l:
        text = re.sub("[\t\n ]", " ", utils.get_page(pages))
        result = re.findall(exp, text)
        for x in result:
            z = x.split(" ")
            if z[0].lower() not in words and z[1].lower() not in words:
                goodWords.append(x)
    wordcounts={}
    for word in goodWords:
        if wordcounts.has_key(word):
            wordcounts[word]+=1
        else:
            wordcounts[word]=1
    person = wordcounts.keys()[0]
    for word in wordcounts:
        if wordcounts[word] > wordcounts[person]:
            person = word
    return person

#print findPerson("Who played Spider Man?")
