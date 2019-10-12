from __future__ import with_statement
import contextlib

try:
    from urllib.parse import urlencode
    
except ImportError:
    from urllib import urlencode
    
try:
    from urllib.request import urlopen
    
except ImportError:
    from urllib2 import urlopen
    
import sys


def url_shorten(url):
    
    req_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(req_url)) as response:
        return response.read().decode('utf-8')
    
def main():
    
    for tinyurl in map(url_shorten,sys.argv[1:]):
        print(tinyurl)
        
if __name__ == "__main__":
    main()