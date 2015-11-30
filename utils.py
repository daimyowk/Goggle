import urllib2, google, bs4, re
from stop_words import get_stop_words

def search(question):
    """
    return result of google search
    
    arguments:
      question: string of question
    
    return:
      array of results 
    """
    result=google.search(question,num=10,start=0,stop=10)
    links=[]
    for r in result:
        links.append(r)
    return links

def get_page(link):
    """
    return contents of link
    
    arguments:
      link: a string
    
    return: 
      string of contents
    """
    try:
        url = urllib2.urlopen(link)
        page = url.read()
        soup = bs4.BeautifulSoup(page,'html')
        raw = soup.get_text()
        return raw
    except:
        return "error"

def search_page(text,question):
    """
    return frequency of ans in text
    
    arguments:
      text: a string that will be parsed for ans
      question: question you want to answer
    
    return: 
      dictionary with ans and their frequency
    """
    #who,where or when question
    if re.search("(W|w)ho",question):
        exp = "[A-Z][a-z][a-z]+ [A-Z][a-z]+"
        result = re.findall(exp,text)
    elif re.search("(W|w)hen",question):
        exp = "([0-9]{1,4}/[0-9]{1,4}/[0-9]{1,4})|([A-Z][a-z]+ [0-9]{0,2}, [0-9]{0,4})"
        result = re.finditer(exp,text)
    elif re.search("(W|w)here",question):
        exp = "(T|t)he [A-Z][a-z]+ ?([A-Z][a-z]+ )+"
        result = re.finditer(exp,text)
    else:
        raise SystemExit(0)
    ans = {}
    if re.search("(W|w)ho",question):
        file = open("words.txt")
        words = file.read()
        goodWords = []
        for x in result:
            z = x.split(" ")
            if z[0].lower() not in words and z[1].lower() not in words:
                goodWords.append(x)
        for word in goodWords:
            if ans.has_key(word):
                ans[word]+=1
            else:
                ans[word]=1
    else:
        for r in result:
            a=r.group(0)
            if a in ans:
                ans[a]+=1;
            else:
                ans[a]=1;
    return ans
            
def find_max(dic):
    """
    return the ans with highest frequencu
    
    arguments:
      dic: a dictionary with ans and frequency
    
    return: 
      ans that occurs most
    """
    frequency=list(dic.values())
    d=list(dic.keys())
    return d[frequency.index(max(frequency))]

def find_answer(question):
    """
    return the ans
    
    argument:
      question: your question
    
    return: 
      the answer
    """
    links=search(question)
    results={}
    for l in links:
        ans=search_page(get_page(l),question)
        for a in ans:
            if a in results:
                results[a]+=1;
            else:
                results[a]=1;
    return find_max(results)

#print find_answer("Who played spiderman?")
#print find_answer("when was the declaration of independence signed?")
#print find_answer("Where is the capital of the united states?")
