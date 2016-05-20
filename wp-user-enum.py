#!/usr/bin/python

#WP User Enum
#Author      : Mr.Doel
#E-email     : doel@indonesiancoder.com
#Version     : 1.1

import urllib2
import sys
import re
from BeautifulSoup import BeautifulSoup

def main():
    for num in range(1,15):
        try:
            response = urllib2.urlopen(url + "/?author=%s" % (num))
            geturi=str(response.geturl())
            if re.search("author=.*", geturi):
                response2=urllib2.urlopen(geturi)
                soup=BeautifulSoup(response2)
                hasil=str(soup.title.string).split('|')
                print hasil[0].lstrip().rstrip()
            elif re.search("/author/",geturi):
                print geturi.split("/author", 1)[1].replace("/", '').lstrip()
        except Exception, e:
            pass
if len(sys.argv) > 1:
    url = sys.argv[1]
    main()
else:
    print "usage :",sys.argv[0], "<URL>"
