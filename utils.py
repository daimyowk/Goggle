import urllib2, google, bs4, re
from stop_words import get_stop_words

def search_page(text,question):
    if re.search("(W|w)ho",question):
        print "find Who"
    elif re.search("(W|w)here",question):
        print "find where"
    elif re.search("(W|w)hen",question):
        print "find when"

