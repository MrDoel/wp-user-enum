#!/usr/bin/python
import urllib2,opt,argparse
from BeautifulSoup import BeautifulSoup

__author__  ="Mr.Doel"
__email__   ="doel@indonesiancoder.com"
__version__ ="1.1"
__license__ ="GPL"

parser=argparse.ArgumentParser(description="WP User Enum",version='1.1')
parser.add_argument('-u','--url',metavar='http[s]://www.site.com',help="Input URL",required=True,type=str)
args=parser.parse_args()
url=args.url
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
main()
