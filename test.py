import urllib2, google, bs4, re

file = open("words.txt")
words = file.read()

q="who played spiderman"
r = google.search(q,num=1,start=0,stop=1)
l=[]
for result in r:
    l.append(result)

#print l[0]

u = urllib2.urlopen(l[0])
page = u.read()
#print page
soup = bs4.BeautifulSoup(page,'html')
raw = soup.get_text()
#print raw
text = re.sub("[\t\n ]"," ",raw)
#print text

exp = "[A-Z][a-z][a-z]+ [A-Z][a-z]+"
result = re.findall(exp,text);
for x in result:
    z = x.split(" ")
    for y in words:
        if z[0].lower() == y or z[1].lower() == y:
            result.remove(x)
print result
